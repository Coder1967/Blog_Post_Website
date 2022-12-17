$(document).ready(function(){

let inputs = {}
let link = "http://127.0.0.1"


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

	    url: link + ":5000/api/v1/users",
	    data: JSON.stringify(inputs),
	    success: function(resp, stat){
		    window.location.replace(link + ":5001/auth/login");
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
