/*takes username and password and queries the api to create a
 * new user if several conditions are met otherwise instruct user
 * on what is missing/wrong about their input
 */

import {HOST, PORT1, PORT2} from './host_and_ports.js'
$(document).ready(function(){

let inputs = {}
let link = HOST;


  $("input[name=button]").click(function(){
    let name = $("input[name=username]").val();
    let password = $("input[name=password]").val();
    let confirm_password = $("input[name=confirm_password]").val();

    let input_list = [name, password, confirm_password];
    let input_str = ['name', 'password', 'confirm_password'];

    for (let i = 0; i < 3; i++){
      if (input_list[i].length > 1){
        inputs[input_str[i]] = input_list[i];
      }
    }

    $.ajax({
	    dataType: "json",
	    contentType: 'application/json',
	    type: "POST",
	    headers: {
		    'Content-Type':'application/json'
	    },

	    url: link + `:${PORT1}/api/v1/users`,
	    data: JSON.stringify(inputs),
	    success: function(resp, stat){
		    window.location.replace(link + `:${PORT2}/auth/login`);
      },
      error: function(error, errorThrow) {
	     $("div[name=error]").addClass("error");
           $("div[name=error]").html('<h4>'+error.responseJSON.error+'<h4>')
       }
    });
  });

	$("div[name=error]").click(function(){
		$("div[name=error]").removeClass("error");
		$("div[name=error]").html('')

	});
});
