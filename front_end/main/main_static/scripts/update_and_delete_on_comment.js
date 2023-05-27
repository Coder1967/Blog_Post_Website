import { PORT1, PORT2, HOST } from './host_and_ports.js';

$(document).ready(function(){
      	let link = HOST
	let user_name = $("span#user").attr("user_name");
	let user_id = $("span#user").attr("user_id");
	let user_pwd = $("span#user").attr("user_pwd");
	let post_id = $("div#display_container").attr("post_id");


        $(".update_comment").click(function(){
		/*
		 * displays a textarea containing the user's previous comment
		 * for user to update their comment
		 */
            	$(this).siblings("input.delete_comment").css("display", "none");
            	$(this).css("display", "none");
            	$(this).siblings("textarea.update_comment_box").css("display", "inline-block");
            	$(this).siblings("input.submit_updated_comment").css("display", "inline-block");

	    let comment_id = $(this).attr("comment_id");
            $.ajax({
            type: "GET",
            url: `${link}:${PORT1}/api/v1/comments/${comment_id}`,
            contentType: "application/json",
            success: function(resp){
              $("textarea.update_comment_box").val(resp.content);
            },
            error: function(err){
              console.log(err);
            }
        });
        });

        $("input.submit_updated_comment").click(function () {
		/*
		 * submits updated comment
		 */
		let comment_id = $(this).attr("comment_id");
		let comment = {}
		comment.content = $(this).siblings("textarea.update_comment_box").val()

          	$.ajax({
          	type: "PUT",
          	data: JSON.stringify(comment),
	   	headers: {
            	"Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
          	},
          	url: `${link}:${PORT1}/api/v1/comments/${comment_id}`,
          	contentType: "application/json",
          	success: function(resp){
            		location.reload(true);
          	},
          	error: function(err){
            console.log(err);
          }
      });
        });

        $(".delete_comment").click(function(){
		/* enables deleting of comment by user */
		let comment_id = $(this).attr("comment_id");
          	$.ajax({
          		type: "DELETE",
          		url: `${link}:${PORT1}/api/v1/comments/${comment_id}`,
          		headers: {
            			"Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
          		},
          		contentType: "application/json",
          		success: function(resp){
            		//refreshing page after removing comment
                	location.reload(true);
         	 },
          	error: function(err){
            	console.log(err);
          	}
      });
    });

	$("input#submit_comment").click(function(){
		/* enables submiting new comment */
		let comment =  {}
		comment.content =  $("textarea#comment_box").val()
		 $.ajax({
          		type: "POST",
          		data: JSON.stringify(comment),
           		headers: {
            			"Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
          		},
          		url: `${link}:${PORT1}/api/v1/posts/${post_id}/${user_id}/comments`,
          		contentType: "application/json",
          		success: function(resp){
		  		$("textarea.comment_box").css('display', 'none');
		  		$("input#submit_comment").css('display', 'none');
            			location.reload(true);
          		},
          		error: function(err){
            		console.log(err);
          		}
      });
	});
});

