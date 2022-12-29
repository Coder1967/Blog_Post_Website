$(document).ready(function(){
  let link = "http://127.0.0.1:"
  let input = {};

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
  		url: link + "5000" + "/api/v1/post_search",
  		data: JSON.stringify(input),
  		success: function(resp, stat){

        if ($("#unordered").html().length > 0)
        {
          $("#unordered").html('')
        }
        for (let res of resp){
          $("#unordered").append(`<l1><a href="${link}5001/main/${res.id}/display_post" class="list">${res.title}</a></li>`);
        }

        },
      error: function(error, errorThrow) {
            console.log(error);
            console.log(errorThrown);
       }
    });
});

});
