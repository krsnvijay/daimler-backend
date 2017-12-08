var token = sessionStorage.tokenid;
var url = "https://daimler-backend.herokuapp.com/api/sos/?ordering=-status";
var url2 = "https://daimler-backend.herokuapp.com/api/comments/";
var json1, json;
$(function () {
    $("#container").hide();
    $('#loader').show();
    fetch(url, {
        method: 'get',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Token ' + token
        }

    }).then(function (response) {
        if (response.ok) {
            response.json().then(function (data) {
                json = data;
                if(json.length>0)
                addItems(json);
                else
                {
                    $("#loader").hide();
                    $("#data-h").show();
                }
            });
        } else {
            console.log('Network request failed with response ' + response.status + ': ' + response.statusText);
        }
    });

    function addItems(json) {
        $("#loader").hide();
        for (var i = json.length - 1; i != 0; i--) {
        	
            
            $("#para").text("" + json[i].content);
            
            $('#index').text(json.length-i);
            $("#comments").text(json[i].comments_count + " comments");
            console.log(json[i].status);
            if(json[i].status)
            {

                $("#status").text("[OPEN]");
                $("#status").css('color','green');
            }
            else
            { 
                $("#status").text("[CLOSED]");
                $("#status").css('color','red');

            }
             $("#container").show();
            
            if(sessionStorage.username==json[i].posted_by)
                 $("#posted_by").text("you posted this "  + jQuery.timeago(json[i].date));
             else
                $("#posted_by").text(json[i].posted_by + ", " + jQuery.timeago(json[i].date));
           
                 $("#container").clone(true, true).insertAfter("#container");
        

        }
        
        $("#para").text("" + json[i].content);
        console.log(json[i].status);
        $('#index').text(json.length-i);
        $("#comments").text(json[i].comments_count + " comments");
        $("#container").show();
         if(json[i].status)
            {
                $("#status").text("[OPEN]");
                $("#status").css('color','green');
            }
            else
            { 
                $("#status").text("[CLOSED]");
                $("#status").css('color','red');

            }
         if(sessionStorage.username==json[i].posted_by)
                 $("#posted_by").text("you posted this "  + jQuery.timeago(json[i].date));
             else
                $("#posted_by").text("By " + json[i].posted_by + ", " + jQuery.timeago(json[i].date));
    
    }

    $("#container").click(function (e) {
        var position = jQuery("p:nth-child(2)", this).text();
        
        if(sessionStorage.username==json[json.length-position].posted_by)
            sessionStorage.choice="ShowToggle";
        sessionStorage.sosid = json[json.length-position].id;
        sessionStorage.desc = json[json.length - position].content;
        sessionStorage.status=json[json.length - position].status;
        sessionStorage.name=   json[json.length - position].name;
        sessionStorage.level=json[json.length - position].level; 
        window.location.replace("/sos-messages.html");


    })

});
