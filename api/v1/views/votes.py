#!/usr/bin/python3
"""
handling of the votes api view
"""
from . import Post, Comment
from . import Vote, User
from flask import abort, jsonify
from . import app_views, storage


@app_views.route("/posts/<an_id>/<user_id>/votes", methods=["GET", "POST"],
                 strict_slashes=False)
def article_votes(an_id, user_id):
    """
    GET: retrives the number of votes of a post or comment
    POST: adds a new vote to the post or comment once per user
    """
    
    article = storage.get(Post, an_id)
    if article is None:
        article = storage.get(Comment, an_id)
    user = storage.get(User, user_id)

    if user is None or article is None:
        abort(404)

    if request.method == "GET":
        resp = {}
        resp["votes"] = len(article.votes)
        return jsonify(resp)

    else:
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


@app_views.route("/user/<user_id>/<an_id>", methods=["POST"], strict_slashes=False)
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
def delete_vote(vote_id):
    """ deletes a vote instance"""
    vote = storage.get(Vote, vote_id)

    if vote is None:
        abort(404)
    storage.delete(vote)
    storage.save()
