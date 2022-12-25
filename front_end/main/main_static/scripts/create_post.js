$(document).ready(function(){
    let inputs = {};

    $("#submit_post").click(function()
    {

      let title = $("#title").val();
      let content = $("#post_content").val();

      if (content.length == 0 || title.length == 0){
        $("div#error").css("display", "block");
        return;
      }

      	inputs.content = content;
      	inputs.title = title;
	let user_id =  $("#submit_post").attr("user_id")

      $.ajax({
  		dataType: "json",
        contentType: 'application/json',
    		type: "POST",
    		url: "http://127.0.0.1:5000/api/v1/users/" + user_id + "/posts",
    		data: JSON.stringify(inputs),
    		success: function(resp, stat){
			window.location.replace("http://127.0.01:5001/main/home")
        },
        error: function(error, errorThrow) {
              console.log(error);
              console.log(errorThrown);
         }
      });
    });

    $("#cancel").click(function(){
        $("#error").css("display", "none");

    });
});
