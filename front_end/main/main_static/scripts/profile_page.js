/* deletes account or send user to the profile update
 * page depending on button clicked
 */
import { PORT1, PORT2, HOST } from './host_and_ports.js';

$(document).ready(function(){
	let user_id = $(".user_info").attr("user_id")
	let link = `${HOST}:${PORT2}/main/`
   
  	$('.update').click(function(){
    	window.location.href = link + "update_profile";
  	});

  	$('#delete').click(function(){
		/* displays a prompt asking user to confirm
		 * the deletion of their account depending on the user's
		 * input, the page is either reloaded or the account deleted
		 */
    		$("#confirm").css("display", "block")
  	});

  	$("#no").click(function(){
    		location.reload(true)
  	});

  	$("#yes").click(function(){
	  	let name = $(".user_info").attr("user_name")
	  	let pwd = $(".user_info").attr("user_pwd")

    	$.ajax({
      	type: "DELETE",
      	url: `${HOST}:${PORT1}/api/v1/users/${user_id}`,
      	headers: {
        	"Authorization": "Basic " + btoa(name + ":" + pwd)
      	},
      	contentType: "application/json",
      	success: function(resp){
        	window.location.replace(`${HOST}:${PORT2}/auth/login`)
      	},
      	error: function(err){
        	console.log(err);
      	}
  	  });

  	});
});
