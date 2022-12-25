$(document).ready(function(){
  // handles everything related to voting on a post
      	let link = "http://127.0.0.1:"
	let user_name = $("div#contain_post").attr("user_name");
	let user_pwd = $("div#contain_post").attr("user_pwd");
	let post_id = $("div#display_container").attr("post_id");
	let user_id = $("div#contain_post").attr("user_id");

      $.ajax({
        type: "POST",
        url: link + "5000/api/v1/users/" + user_id + '/' + post_id +"/voted",
        contentType: "application/json",
        success: function(resp){
          if (resp.value){
              $("#vote_icon").attr('src', "../main_static/images/upvote.png")
            $("#vote_icon").click(function() {
                $.ajax({
                type: "DELETE",
                url: link + "5000/api/v1/votes/" + resp.vote_id,
                headers: {
                  "Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
                },
                contentType: "application/json",
                success: function(resp){
                  //refreshing page after removing vote
                      $("#vote_icon").attr('src',  "../main_static/images/vote.png")
                      location.reload(true);
                },
                error: function(err){
                  console.log(err);
                }

            });
          });
        }

          else{
              $("#vote_icon").attr('src',  "../main_static/images/vote.png")
            $("#vote_icon").click(function() {
                $.ajax({
                type: "POST",
                url: link + "5000/api/v1/posts/" + post_id + "/" + user_id + "/votes",
                headers: {
                  "Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
                },
                contentType: "application/json",
                success: function(resp){
                      $("#vote_icon").attr('src',  "../main_static/images/upvote.png");
                      //refreshing page after voting
                      location.reload(true)
                },
                error: function(err){
                  console.log(err);
                }

            });
          });
        }

        },
        error: function(err){
          console.log(err);
        }
      });


});
