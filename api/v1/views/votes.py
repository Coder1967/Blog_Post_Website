#!/usr/bin/python3
"""
handling of the votes api view
"""
from . import Post, Comment
from . import Vote, User
from flask import abort, jsonify, current_app, g
from . import app_views, storage
with current_app.app_context():
    from .secure import auth, verify_password


@app_views.route("/posts/<an_id>/votes", strict_slashes=False)
def article_votes(an_id):
    """
    GET: retrives the votes of a post or comment
    """
    votes = []
    article = storage.get(Post, an_id)
    if article is None:
        article = storage.get(Comment, an_id)

    if article is None:
        abort(404)

    for vote in article.votes:
        votes.append(vote.to_dict())
    return jsonify(votes)


@app_views.route("/posts/<an_id>/<user_id>/votes", methods=["POST"],
                 strict_slashes=False)
def post_vote(an_id, user_id):
    """
    POST: adds a new vote to the post or comment once per user
    """
    user = storage.get(User, user_id)
    article = storage.get(Post, an_id)
    if article is None:
        article = storage.get(Comment, an_id)

    if article is None or user is None:
        abort(404)

    for vote in article.votes:
        if vote.user_id == user.id:
            abort(400, description="already voted on post")
    kwargs = {"user_id": user_id}
    if type(article).__name__ == "Post":
        kwargs["post_id"] = an_id
    else:
        kwargs["comment_id"] = an_id
    vote = Vote(**kwargs)
    vote.save()
    return jsonify(vote.to_dict()), 201


@app_views.route("/user/<user_id>/<an_id>/voted", methods=["POST"], strict_slashes=False)
def has_voted(user_id, an_id):
    """ checks if user has voted"""
    article = storage.get(Post, an_id)
    if article is None:
        article = storage.get(Comment, an_id)
    user = storage.get(User, user_id)

    if user is None or article is None:
        abort(404)

    for votes in article.votes:
        if votes.user_id == user_id:
            return jsonify({"value": True})
    return jsonify({"value": False})


@app_views.route("/votes/<vote_id>", methods=["DELETE"], strict_slashes=False)
@auth.login_required
def delete_vote(vote_id):
    """ deletes a vote instance"""
    vote = storage.get(Vote, vote_id)
    if vote is None:
        abort(404)

    """ making sure only the owner of the vote is allowed"""
    if g.user.name != vote.voter.name:
        abort(401)

    storage.delete(vote)
    storage.save()
