var token = sessionStorage.tokenid;
var json;
var url = "https://daimler-backend.herokuapp.com/api/comments/?posted_by=&sosid=" + sessionStorage.sosid + "&date=&partid=";
var urlpost = "https://daimler-backend.herokuapp.com/api/comments/";
var urlsos="https://daimler-backend.herokuapp.com/api/sos/"+sessionStorage.sosid+"/";
$(function () {
    console.log(sessionStorage.choice);
    
    if(sessionStorage.choice!="ShowToggle")
    {
        $("#toggle").hide();
        $('#data-h').show();
        $("#del").hide();
    }

    $("#description").text(sessionStorage.desc);
    console.log(sessionStorage.status);
    if(sessionStorage.status=="true")
    {
        $("#status").prop('checked',true);
        $("#input").show();
    }
    
    fetch(url, {
        method: "get",
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
                    var div = document.getElementById('messageContainer');
                    if (div)
                        div.parentNode.removeChild(div);


                }
            });
        } else {
            console.log("Error")
        }
    })

    function addItems(json) {
        
        for (var i = 0; i <json.length-1; i++) {

            $("#message").text(json[i].content);
            $("#user").text(json[i].posted_by);
            $("#messageContainer").show();
             if(json[i].media!= undefined)
           {
           	openlink(json[i].media);
           }
            
            $("#messageContainer").clone().insertAfter("#messageContainer");

        }
         $("#messageContainer").show();
        $("#message").text(json[i].content);
        $("#user").text(json[i].posted_by);
         if(json[i].media!= undefined)
           {
           	openlink(json[i].media);
           }
           if(sessionStorage.status=="false")
           {
                
                
    
           }

    }
    $("#blah").click(function(event){
  	if(sessionStorage.file!=undefined)
  	window.open(sessionStorage.file);
  });
    $("#status").change(function(){
       var formData= new FormData();
       formData.append("name",sessionStorage.name);
       formData.append("content",sessionStorage.desc);
       formData.append("level",sessionStorage.level);
       formData.append("status",this.checked);
       var xhrsos= new XMLHttpRequest();
       xhrsos.open('PUT',urlsos,true);
       //xhrsos.setRequestHeader('Content-Type','multipart/form-data');
       xhrsos.setRequestHeader('Authorization', 'Token ' + token);
        xhrsos.onload = function () {
            console.log(xhrsos.status);
            if (xhrsos.status === 200) {
                window.location.replace("/sos-dashboard.html");
                $("#input").hide();
                $('#data-h').show();
                alert("Thread status changed");
            } else {
                alert('An error occurred!');
            }
        };
        xhrsos.send(formData);
    });
    $("#delete").click(function(event){
        event.preventDefault();

        var xhr= new XMLHttpRequest();
        
        xhr.open('DELETE',urlsos, true);
        xhr.setRequestHeader('Authorization', 'Token ' + token);
        xhr.onload= function () {
           if(xhr.status==204)
           {
            alert("Thread deleted succesfully")
            window.location.replace("/sos-dashboard.html");
           }
           else
           {
            alert("Error occured!");
           }
        }
        xhr.send();
        
    })
    $("#send").click(function (event) {
        event.preventDefault();
        var text = $("#icon_prefix").val();

        var form = document.getElementById('message-form');
        var formData = new FormData();
        var fileSelect = document.getElementById('file-select');
        var file = fileSelect.files;
        formData.append("content", text);
        formData.append("sosid", "https://daimler-backend.herokuapp.com/api/sos/" + sessionStorage.sosid + "/");


        var xhr = new XMLHttpRequest();
        xhr.open('POST', urlpost, true);
        //xhr.setRequestHeader('Content-Type','multipart/form-data');
        xhr.setRequestHeader('Authorization', 'Token ' + token);

        for (var i of formData.values()) {
            console.log(i);
        }
        xhr.onload = function () {
            console.log(xhr.status);
            if (xhr.status === 201) {
                window.location.replace("/sos-messages.html");
            } else {
                alert('An error occurred!');
            }
        };
        xhr.send(formData);
    })
 function openlink(link)
  {
  	    var a = document.createElement('a');
        var linkText = document.createTextNode("\tClick to view the file");
        a.appendChild(linkText);
        a.title = "\nClick to view the file";
        a.href = link;
        a.target="_blank";
        document.getElementById("message").append(a);
  }
 

})