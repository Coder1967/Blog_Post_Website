import { PORT1, PORT2, HOST } from './host_and_ports.js';

$(document).ready(function(){

	//handles saving post entered by user into the database using the api
    	let inputs = {};

    	$("#submit_post").click(function()
    	{

      		let title = $("#title").val();
      		let content = $("#post_content").val();

      		if (content.length == 0 || title.length == 0){
			/*makes the error message visible whenever
			 * both title and content of post is not provided
			 */
        		$("div#error").css("display", "block");
        		return;
  		}

      		inputs.content = content;
      		inputs.title = title;
		let user_id =  $("#submit_post").attr("user_id")
		/*sends post from the user to the rest api for storage
		 */

      		$.ajax({
  			dataType: "json",
        		contentType: 'application/json',
    			type: "POST",
    			url: `${HOST}:${PORT1}/api/v1/users/${user_id}/posts`,
    			data: JSON.stringify(inputs),
    			success: function(resp, stat){
				window.location.replace(`${HOST}:${PORT2}/main/home`)
        	},
        	error: function(error, errorThrow) {
              		console.log(error);
              		console.log(errorThrown);
         	}
      	});
    	});
	/* makes the error message vanish when it is clicked on*/
    	$("#cancel").click(function(){
        	$("#error").css("display", "none");

    	});
});
