$(document).ready(function(){
	let inputs = {};
	let link = "http://127.0.0.1";

	$("input[name=file]").change(function(){
		// making sure a file was actually selected before enabling button
		$("input.update").attr('type', 'submit')
		$("input.update").css('background-color', 'purple')

	});

	$("input[name=password]").change(function(){
		//allows user to change their password
		 $("input.update").css('background-color', 'purple')
		 $("input.update").click(function(){
    			inputs.password = $("input[name=password]").val();
    			inputs.confirm_password = $("input[name=confirm_password]").val();
			let user_id =  $("input[name=password]").attr('user_id')
			let user_name = $("input[name=confirm_password]").attr('user_name');
			let user_pwd = $("input[name=file]").attr('user_pwd')
	

    			$.ajax({
            			dataType: "json",
            			contentType: 'application/json',
            			type: "PUT",
				url: link + `:5000/api/v1/users/${user_id}`,
            			headers: {
		    			"Authorization": "Basic " + btoa(user_name + ":" + user_pwd)
          
            			},

            			data: JSON.stringify(inputs),
            			success: function(resp, stat){
                    			window.location.replace(link + ":5001/main/home");
      			},
      			error: function(error, errorThrow) {
             			$("div[name=error]").addClass("error");
           			$("div[name=error]").html('<h4>'+error.responseJSON.error+'<h4>')
       		}
    				});
  			});
		});

        $("div[name=error]").click(function(){
		// removes error displayed
                $("div[name=error]").removeClass("error");
                $("div[name=error]").html('')

        });
});
