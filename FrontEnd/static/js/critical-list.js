var url = "https://daimler-backend.herokuapp.com/api/critical_list/critical_parts/";

var data = [];
var json;

//global variable that holds a reference to the node that displays parts
var tableRow;

var token = sessionStorage.tokenid || "83cc351e4ec002a30f5fbe3e768cc4874263e9dd";

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1;
var yyyy = today.getFullYear();

if (dd < 10) {
    dd = '0' + dd
}

if (mm < 10) {
    mm = '0' + mm
}

date = yyyy + '-' + mm + '-' + dd;

var ctx = document.getElementById('myChart').getContext('2d');





$(function () {

    getData();

    $('#mdt').click(function () {
        sessionStorage.selection = "Giftson";
        window.location.replace("/critical-list-detail.html");

    });
    $('#hdt').click(function () {
        sessionStorage.selection = "Arulselvan";
        window.location.replace("/critical-list-detail.html");
    });
    $('#axle').click(function () {

        var cardTitle = "AXLE";
        sessionStorage.selection = "Joshna";
        console.log(cardTitle);
        window.location.replace("/critical-list-detail.html");

    });
    $('#casting-and-forging').click(function () {

        var cardTitle = "CASTING AND FORGING";
        sessionStorage.selection = "Premkumar";
        console.log(cardTitle);
        window.location.replace("/critical-list-detail.html");

    });
    $('#transmission').click(function () {

                var cardTitle = "TRANSMISSION";
                sessionStorage.selection = "Balaji";
                console.log(cardTitle);
                window.location.replace("/critical-list-detail.html");

            });

    $('.datepicker').pickadate({
                selectMonths: true, // Creates a dropdown to control month
                selectYears: 15, // Creates a dropdown of 15 years to control year,
                today: 'Today',
                clear: 'Clear',
                close: 'Ok',
                closeOnSelect: true // Close upon selecting a date,
              });

                //For storing a reference to the node that displays parts
                  var tableContainer = document.getElementById('table');
                  var childNodes = tableContainer.children;
                  console.log(childNodes);

                   tableRow = childNodes[1].childNodes[1];


            //to select a date
            $('#sort-selection').click(function(){

              var sortsCard = document.getElementById('sort-choices');

              if($('#sort-choices').css('display') == 'none') {
                sortsCard.style.removeProperty('display');
                  console.log(sortsCard.children);

              }
              else{
                $('#sort-choices').css('display','none');

              }

              $('#apply-btn').click(function(){
                  sortsCard.setAttribute('style','display: none;');

                  var sortSelected = $('input[name=dates]:checked').next().text();
                  console.log(sortSelected);

                  var year = $('.datepicker').pickadate('picker').get('highlight', 'yyyy');
                  var month = $('.datepicker').pickadate('picker').get('highlight', 'mm');
                  var day = $('.datepicker').pickadate('picker').get('highlight', 'dd');
                  date = year + '-' + month + '-' + day;
                  sessionStorage.date = date;



                  getData();
              });
            });

            $('#next').click(function(e){
              var d= $('#date').text();
              dd= parseInt(d.substr(8,9));
              dd++;
              if(dd==31) dd=1;
              date = yyyy + '-' + mm + '-' + dd;

              getData();
              e.stopPropagation();
            });
            $('#prev').click(function(e){
              var d= $('#date').text();
              dd= parseInt(d.substr(8,9));

              dd--;
              if(dd==0) dd=31;
              date = yyyy + '-' + mm + '-' + dd;
              getData();
              e.stopPropagation();
            });


});

function getData() {
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
                            alert(json);
                            console.log(json);
                            dataForChart(json);
                            addItems(json);
                            updateDisplay(json,date);

                        });
                    } else {
                        console.log('Network request failed with response ' + response.status + ': ' + response.statusText);
                    }
                });
            }

            function dataForChart(json) {
                var partnumber = [];
                var quantityAvailable = [];
                var plannedVehicleQuantity = [];
                var dicv = [];

                for (var i = 0; i < json.length; i++) {

                    if (i == 4) break;

                    for (var prop in json[i]) {
                        if (prop == 'part_number')
                            partnumber.push(json[i][prop]);

                        else if (prop === 'quantity')
                            quantityAvailable.push(json[i][prop]);

                        else if (prop === 'eta_dicv')
                            dicv.push(json[i][prop]);

                        else if (prop === 'planned_vehicle_qty')
                            plannedVehicleQuantity.push(json[i][prop]);


                    }
                    console.log(quantityAvailable);

                }
                var chart = new Chart(ctx, {
                    // The type of chart we want to create
                    type: 'bar',
                    scaleFontColor: '#fffffff',

                    // The data for our dataset
                    data: {
                        labels: partnumber,
                        datasets: [{
                            label: "Quantity Avl",
                            backgroundColor: 'rgb(210, 48, 48)',
                            borderColor: 'rgb(210, 48, 48)',
                            data: quantityAvailable,
                        },
                                   {
                                       label: "Planned Vehicle Qty",
                                       backgroundColor: 'rgb(200, 200, 136)',
                                       borderColor: 'rgb(200, 200, 136)',
                                       data: plannedVehicleQuantity,
                                   },
                                  ],
                    },

                    // Configuration options go here
                    options: {
                        scaleFontColor: '#ffffff',
                        responsive: "true",
                        layout: {
                            padding: {
                                left: 20,
                                right: 20,
                                top: 10,
                                bottom: 10
                            }
                        },
                        legend: {
                            labels: {
                                fontColor: "#ffffff",
                            }
                        },

                        scales: {
                            xAxes: [{
                                ticks: {
                                    fontColor: "#ffffff",
                                }
                            }],
                            yAxes: [{
                                ticks: {
                                    fontColor: "#ffffff",
                                    beginAtZero: true
                                }
                            }]
                        }
                    }
                });
            }

function updateDisplay(json, date) {

    $('#date').text(date);

    var container = document.getElementById('table');
    var children = container.children;
    var partContainer = children[1] //tbody
    var partDetails = partContainer.children;
    console.log(partDetails);

    if (json.length > 0) {

    for (var i = 0; i < json.length; i++) {
        console.log(String(i) + ' ' + json.length)
        var j = 0;
        for (var prop in json[i]) {

        if (prop === "url") continue;

        var parts = json[i];

        //traverse the DOM and get the td cell
        var cells = partDetails[i].children;

        if (prop === 'part_number') {
            cells[0].innerText = parts[prop];
        } else if (prop === 'starred') {

            if (parts[prop] === true) {
                cells[4].innerHTML =
                    "<img src='resources/images/filled_star.png' id='image' onClick='editCell'>";
            } else {
                cells[4].innerHTML =
                    "<img src='resources/images/star2.png' id='image' onClick='editCell'>";
            }
        }else if (prop ==='pmc'){
          cells[3].innerText = parts[prop];
        } else if (prop === 'supplier_name') {
            cells[1].innerText = parts[prop];
        } else if (prop === 'shop') {
            cells[2].innerText = parts[prop];
        } else if (prop === "status") {

            if (parts[prop] === 3) {
                partDetails[i].setAttribute('class', 'red lighten-2');
            } else if (parts[prop] === 2) {
                partDetails[i].setAttribute('class', 'yellow lighten-2');
            } else {
                partDetails[i].setAttribute('class', 'green lighten-2');
            }

        }
        cells[5].innerHTML = "<i class='material-icons' href='modal_notify modal-trigger'>send</i>";
    }
        }
    }
}

function addItems(list) {

var tableContainer = document.getElementById('table');
var childNodes = tableContainer.children;
console.log(childNodes);

var tableBody = childNodes[1];

while (tableBody.firstChild) {
    tableBody.removeChild(tableBody.firstChild);
}
console.log(list.length);
if (list.length > 0) {
    for (var i = 0; i < list.length; i++) {
        var newRow = tableRow.cloneNode(true);
        var cells = newRow.children;

        for(var j=0; j<cells.length; j++){
            cells[j].onclick = editCell;
      }
        tableBody.appendChild(newRow);
    }
} else {

    var newRow = tableRow.cloneNode(true);
    tableBody.appendChild(newRow);

 }
}

function editCell(event){

    if(event.target.tagName === 'IMG'){

        var cell = event.target.parentNode;
      event.stopPropagation();
      var rowIndex = event.target.parentNode.parentNode.rowIndex;
      console.log(rowIndex);
      rowIndex -= 1;
      var imageSource = event.target.src;
      var fileName = imageSource.substr(imageSource.lastIndexOf('/') + 1);
      if(fileName === "star2.png"){
      star(cell,rowIndex);
      // event.target.src= "resources/images/filled_star.png";
      event.target.parentNode.innerHTML = "<svg class='spinner' width='20px' height='20px' viewBox='0 0 66 66' xmlns='http://www.w3.org/2000/svg'><circle class='circle-loader' fill='none' stroke-width='6' stroke-linecap='round' cx='33' cy='33' r='30'></circle></svg>";
    }
    else{
      unStar(cell,rowIndex);
      // event.target.src = "resources/images/star2.png";
      event.target.parentNode.innerHTML = "<svg class='spinner' width='20px' height='20px' viewBox='0 0 66 66' xmlns='http://www.w3.org/2000/svg'><circle class='circle-loader' fill='none' stroke-width='6' stroke-linecap='round' cx='33' cy='33' r='30'></circle></svg>";
    }
  }
  else {
        event.target.setAttribute('class', 'modal-trigger');
        event.target.setAttribute('href', '#modal1');

        var rowIndex = event.target.parentNode.rowIndex;
        var tableContainer = document.getElementById('table');
        var childNodes = tableContainer.children;
        var tableBody = childNodes[1];
        var rows = tableBody.children;

        console.log(rows);

        populateAndEditModal(rowIndex);

  }
}

function star(cell,rowIndex){
  var url = "https://daimler-backend.herokuapp.com/api/current_user/starred_parts/";

  var formData = new FormData();

  partNumber = json[rowIndex]['part_number'];

  formData.append('part_number', partNumber);

  var xhr = new XMLHttpRequest();

// Open the connection.
xhr.open('PATCH', url, true);

xhr.setRequestHeader('Authorization','Token '+token);

// Set up a handler for when the request finishes.
xhr.onload = function () {
  console.log(xhr.status);
  if (xhr.status === 200) {
    //alert('successful');
    cell.innerHTML = "<img src='resources/images/filled_star.png' id='image' onClick='editCell'>";
  }
  else {
    alert('An error occurred!');
  }
};

// Send the Data.
xhr.send(formData);
}

function unStar(cell,rowIndex){

  var url = "https://daimler-backend.herokuapp.com/api/current_user/starred_parts/";

  var formData = new FormData();

  partNumber = json[rowIndex]['part_number'];

  formData.append('part_number', partNumber);

  var xhr = new XMLHttpRequest();

// Open the connection.
xhr.open('DELETE', url, true);

xhr.setRequestHeader('Authorization','Token '+token);

// Set up a handler for when the request finishes.
xhr.onload = function () {
  console.log(xhr.status);
  if (xhr.status === 200) {
    //alert('successful');
    cell.innerHTML = "<img src='resources/images/star2.png' id='image' onClick='editCell'>";

  }
  else {
    alert('An error occurred!');
  }
};

// Send the Data.
xhr.send(formData);

}

function populateAndEditModal(rowIndex){

// populate the input fields with values from the api response.
    $('#part_name').text(json[rowIndex-1]['shop']);
    $('#part_number').val(json[rowIndex-1]['part_number']);
    $('#description').val(json[rowIndex-1]['description']);
    $('#supplier_name').val(json[rowIndex-1]['supplier_name']);
    $('#variants').val(json[rowIndex-1]['variants']);
    $('#count').val(json[rowIndex-1]['count']);
    $('#reported_on').val(json[rowIndex-1]['reported_on']);
    $('#short_on').val(json[rowIndex-1]['short_on']);
    $('#shop').val(json[rowIndex-1]['shop']);
    $('#pmc').val(json[rowIndex-1]['pmc']);
    $('#team').val(json[rowIndex-1]['team']);
    $('#backlog').val(json[rowIndex-1]['backlog']);
    $('#region').val(json[rowIndex-1]['region']);
    $('#unloading_point').val(json[rowIndex-1]['unloading_point']);
    $('#p_q').val(json[rowIndex-1]['p_q']);
    $('#quantity').val(json[rowIndex-1]['quantity']);
    $('#quantity_expected').val(json[rowIndex-1]['quantity_expected']);
    $('#planned_vehicle_qty').val(json[rowIndex-1]['planned_vehicle_qty']);
    $('#eta_dicv').val(json[rowIndex-1]['eta_dicv']);
    $('#truck_details').val(json[rowIndex-1]['truck_details']);
    $('#shortage_reason').val(json[rowIndex-1]['shortage_reason']);
    $('#status').val(json[rowIndex-1]['status']);

    if(json[rowIndex-1]['status'] === 3)
        $('#critical-radio-btn').attr('checked','checked');
    else if(json[rowIndex-1]['status'] === 2)
        $('#warning-radio-btn').attr('checked','checked');
        else
            $('#normal-radio-btn').attr('checked','checked');

}
