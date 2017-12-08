var urlnav="https://daimler-backend.herokuapp.com/rest-auth/logout/"
$("#uname").text(sessionStorage.username);
$("#uemail").text(sessionStorage.email);
$("#sos-nav").click(function(event){
     window.location.replace("/sos-dashboard.html");
});
$('#critical-list-nav').click(function () {
    // sessionStorage.selection = "MDT ENGINE";
    window.location.replace("/critical-list.html");

});
$('#mdt-nav').click(function () {
    sessionStorage.selection = "Giftson";
    window.location.replace("/critical-list-detail.html");

});

$("#not").click(function(){
    sessionStorage['goBackTo'] = window.location.href;
    window.location.replace("/notifications.html");
});

$('#hdt-nav').click(function () {
        sessionStorage.selection = "Arulselvan";
        window.location.replace("/critical-list-detail.html");
});
$('#axle-nav').click(function () {

    var cardTitle = "AXLE";
    sessionStorage.selection = "Joshna";
    console.log(cardTitle);
    window.location.replace("/critical-list-detail.html");

});
$('#casting-and-forging-nav').click(function () {

    var cardTitle = "CASTING AND FORGING";
    sessionStorage.selection = "Premkumar";
    console.log(cardTitle);
    window.location.replace("/critical-list-detail.html");
});
$('#transmission-nav').click(function () {
    
        var cardTitle = "TRANSMISSION";
        sessionStorage.selection = "Balaji";
        console.log(cardTitle);
        window.location.replace("/critical-list-detail.html");
    
    });
$('#logout-nav').click(function(){
  var xhr = new XMLHttpRequest();
  xhr.open('POST', urlnav, true);
  sessionStorage.choice="";
  xhr.onload = function () {
            if(xhr.status=200)
                window.location.replace("/");
            else
                alert("Unable to log out");
           }
  xhr.send();
});


function backBtn(){
    window.location.href = sessionStorage['goBackTo'];
}