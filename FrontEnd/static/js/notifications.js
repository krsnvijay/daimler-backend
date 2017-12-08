var url = "https://daimler-backend.herokuapp.com/api/comments/?userid="+sessionStorage.userid;
var token= sessionStorage.tokenid;
$(function(){
	fetch(url, {
		method:"get",
		 headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Token ' + token
        }
	}).then(function (response) {
        if (response.ok) {
            response.json().then(function (data) {
                json = data;
                console.log(json);
                if (json.length != 0)
                    addItems(json);
                else {
                    var div = document.getElementById('item');
                    if (div)
                        div.parentNode.removeChild(div);
                    $("#data-h").show();

                }
            });
        } else {
            console.log("Error")
        }
    })
  function addItems(json)
  {
     for(i=json.length-1;i!=0;i--)
     {
     	$("#content").text(json[i].content);
     	$("#item").show();
     	$("#item").clone(true,true).insertAfter("#content");
     }
     $("#item").show();
     $("#content").text(json[i].content);
  }
})