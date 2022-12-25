$(document).ready(function(){
        let link = "http://127.0.0.1:"
        let user_name = $("div#display_container").attr("poster_name");
        let user_pwd = $("div#display_container").attr("poster_pwd");
        let post_id = $("div#display_container").attr("post_id");
        let user_id = $("div#display_container").attr("poster_id");


        $("input#update_post").click(function(){
          $("div#display_container").css("display", "none");
          $("img#vote_icon").css("display", "none");
          $("img#comment_icon").css("display", "none");
          $("input#delete_post").css("display", "none");
          $("input#update_post").css("display", "none");
          $("span.number_of").css("display", "none");
          $("textarea#update_post_box").css("display", "inline-block");
          $("input#submit_post").css("display", "inline-block")
          $("input#update_post_title").css("display", "inline-block")

          $.ajax({
          type: "GET",
          url: link + "5000/api/v1/posts/" + post_id,
          contentType: "application/json",
          success: function(resp){
            $("input#update_post_title").val(resp.title);
            $("textarea#update_post_box").val(resp.content);
          },
          error: function(err){
            console.log(err);
          }
      });

        });

        $("#delete_post").click(function(){
          $.ajax({
          type: "DELETE",
          url: link + "5000/api/v1/posts/" + post_id,
          headers: {
            "Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
          },
          contentType: "application/json",
          success: function(resp){
            //going back to home page after removing post
                window.location.replace("http://127.0.0.1:5001/main/home");
          },
          error: function(err){
            console.log(err);
          }

      });
    });

	$("input#submit_post").click(function(){
		let post = {}
		post.title = $("input#update_post_title").val()
		post.content = $("textarea#update_post_box").val()
          $.ajax({
	  data: JSON.stringify(post),
          type: "PUT",
          url: link + "5000/api/v1/posts/" + post_id,
          headers: {
            "Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
          },
          contentType: "application/json",
          success: function(resp){
            //going back to home page after removing post
                window.location.reload(true);
          },
          error: function(err){
            console.log(err);
          }

      });
    });

      // makes comment box and button appear or disappear
    $("#comment_icon").click(function(){

        if ($("#comment_box").css("display") == "none"){
        $("#comment_box").css("display", "inline-block");
        $("#submit_comment").css("display", "inline-block");
      }
      else{
        $("#comment_box").css("display", "none");
        $("#submit_comment").css("display", "none");
      }

    });
});

