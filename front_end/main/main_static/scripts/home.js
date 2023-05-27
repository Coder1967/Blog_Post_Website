import { PORT1, PORT2, HOST } from './host_and_ports.js';

$(document).ready(function(){
  	let input = {};

	/*handles the search functionality*/

  	$("button[name=search_btn]").click(function(){
	  	let search = $("input[type=search]").val();
    		if (search.length < 1){
      		return;
    	}

    	input.query = search;
    	$.ajax({
		dataType: "json",
      		contentType: 'application/json',
  		type: "POST",
  		url: `${HOST}:${PORT1}/api/v1/post_search`,
  		data: JSON.stringify(input),
  		success: function(resp, stat){
			/* if the result of a previous query is still displayed, it gets
			 * removed and replaced with the result of the latest one
			 */

        		if ($("#unordered").html().length > 0){
          			$("#unordered").html('')
        		}
        		for (let res of resp){
          		$("#unordered").append(`<l1><a href="${HOST}:${PORT2}/main/${res.id}/display_post" class="list">${res.title}</a></li>`);
        	}

        	},
      		error: function(error, errorThrow) {
            	console.log(error);
            	console.log(errorThrown);
       		}
    	});
});

});
