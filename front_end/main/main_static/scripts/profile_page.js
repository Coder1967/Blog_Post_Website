$(document).ready(function(){
	let user_id = $(".user_info").attr("user_id")
	let link = 'http://127.0.0.1:5001/main/'
   
  	$('.update').click(function(){
    	window.location.href = link + "update_profile";
  	});

  	$('#delete').click(function(){
    	$("#confirm").css("display", "block")
  	});

  	$("#no").click(function(){
    	window.location.replace(link + user_id + '/profile')
  	});

  	$("#yes").click(function(){
	  	let name = $(".user_info").attr("user_name")
	  	let pwd = $(".user_info").attr("user_pwd")

    	$.ajax({
      	type: "DELETE",
      	url: "http://127.0.0.1:5000/api/v1/users/" + user_id,
      	headers: {
        	"Authorization": "Basic " + btoa(name + ":" + pwd)
      	},
      	contentType: "application/json",
      	success: function(resp){
        	window.location.replace("http://127.0.0.1:5001/auth/login")
      	},
      	error: function(err){
        	console.log(err);
      	}
  	  });

  	});
});
