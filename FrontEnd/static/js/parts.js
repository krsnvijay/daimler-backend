var url = "https://daimler-backend.herokuapp.com/api/parts/?ordering=short_on,-status&pmc=";

var token = sessionStorage.tokenid || "83cc351e4ec002a30f5fbe3e768cc4874263e9dd";
console.log(token);
var json;
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1;
var yyyy = today.getFullYear();

//global variable that holds a reference to the node that displays parts
var tableRow;

// global variable that is used in patch request for starring.
var partNumber;

if(dd<10) {
    dd = '0'+dd
}

if(mm<10) {
    mm = '0'+mm
}

var pmcvalues = {
            'Arulselvan': 'HDT ENGINE',
            'Balaji': 'TRANSMISSION',
            'Joshna': 'AXLE',
            'Giftson': 'MDT ENGINE',
            'Premkumar': 'CASTING AND FORGING',
        };
var selection = sessionStorage.selection || "MDT ENGINE";
console.log(selection);
var shopType = pmcvalues[selection]; // For card Title
var date = sessionStorage.date || today;
selection = selection.replace(/ /g,'%20');

date = yyyy + '-' + mm + '-' + dd;
// if(token==undefined) window.location="http://localhost:3000";
$(function(){

   //get response from api
  getData();

  $('#shop_type').html(shopType);


//For storing a reference to the node that displays parts
      var tableContainer = document.getElementById('table');
      var childNodes = tableContainer.children;
      console.log(childNodes);

       tableRow = childNodes[1].childNodes[1];



  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: true // Close upon selecting a date,
  });

  // select the radio button when list item is clicked.
  $(".dropdown-content > li").click(function(){
    $(".dropdown-content > li").find('input[type="radio"]').removeAttr('checked');
    $(this).find('input[type="radio"]').attr('checked','checked');

    var label = $(this).find('label');
    console.log(label);
    if(label[0].innerText === 'All'){
      getData();
      updateDisplay(json,date);
    }
    else if(label[0].innerText === 'Critical'){
      getData();
      updateDisplay(json,date);
    }
    else if(label[0].innerText === 'Starred'){
      //getData();
      starSort();
    }

});

  $('#critical-sort-radio-btn').click(function(){
    getData();
    updateDisplay(json,date);
  });

  $('#starred-radio-btn').click(function(){
    getData();
    starSort();
  });

  $('#all-radio-btn').click(function(){
    getData();
    updateDisplay(json,date);
  });



  // var picker = $input.pickadate('picker');
  // date = picker.get('select', 'yyyy/mm/dd');
  // console.log(date);

  // $('.card.hoverable').on('click', function(e){
  //   return false;
  // });

  // $('td.clickable').click(function(e){
  //   e.stopPropagation();
  //   alert(e.target.value);
  // });

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

function getData(){
fetch(url + selection+"&short_on="+date, {
   method: "get",
                headers: {
                    'Content-Type' : 'application/x-www-form-urlencoded',
                    'Authorization' : 'Token '+token
                }
            }).then(function(response){
              if(response.ok){
                response.json().then(function(data){
                    //json = data;
                    console.log(json);

                        //method to add individual parts under a part type
                          addItems(data);
                          updateChart(data);
                          updateDisplay(data, date);
                 });
              }
              else {
                 console.log('Network request failed with response ' + response.status + ': ' + response.statusText);
              }
            });
        }

function updateDisplay(jsonResponse, date){

  json = jsonResponse;
$('#date').text(date);

var container = document.getElementById('table');
var children = container.children;

// var partType = children[0].childNodes[1].childNodes[1].childNodes[1]; //card title
// partType.innerHTML = selection.replace(/%20/g," ");
var partContainer = children[1] //tbody
var partDetails = partContainer.children;

console.log(partDetails);

var card_ref = document.getElementById('card-cont');
var no_data = document.getElementById('data-h');

if(json.length>0)
{
  no_data.setAttribute('style','display: none;');
   card_ref.removeAttribute('style','display: none;');
  for(var i=0; i<json.length; i++){


  var j=0;
  for(var prop in jsonResponse[i]){

    if(prop === "url")continue;

    var parts = jsonResponse[i];


    //traverse the DOM and get the td cell
    var cells = partDetails[i].children;

    if(prop === 'part_number'){
        cells[0].innerText = parts[prop];
    }
    else if(prop === 'starred'){

        if(parts[prop]===true)
        {
          cells[3].innerHTML = "<img src='resources/images/filled_star.png' id='image' onClick='editCell'>";
        }
         else
            {
          cells[3].innerHTML = "<img src='resources/images/star2.png' id='image' onClick='editCell'>";
            }
        }


    else if(prop === 'supplier_name'){
        cells[1].innerText = parts[prop];
        }
    else if(prop === 'shop'){
        cells[2].innerText = parts[prop];
        }
    else if(prop === "status"){

        if(parts[prop] === 3){
        partDetails[i].setAttribute('class', 'red lighten-2');
        }
        else if(parts[prop] === 2){
        partDetails[i].setAttribute('class', 'yellow lighten-2');
        }
        else {
        partDetails[i].setAttribute('class', 'green lighten-2');
      }

    }
  }

}
}
else
  {
     card_ref.setAttribute('style','display: none;');
     no_data.removeAttribute('style','display: none;');
  }

}

function addItems(list){

      var tableContainer = document.getElementById('table');
      var childNodes = tableContainer.children;
      console.log(childNodes);

      var tableBody = childNodes[1];

        while (tableBody.firstChild) {
        tableBody.removeChild(tableBody.firstChild);
      }
      console.log(list.length);
      if(list.length>0){
        for( var i=0; i<list.length; i++)
      {
          var newRow = tableRow.cloneNode(true);
          var cells = newRow.children;
          for(var j=0; j<cells.length; j++){
            cells[j].onclick = editCell;
      }

          tableBody.appendChild(newRow);
      }
    }else{

          var newRow = tableRow.cloneNode(true);
          tableBody.appendChild(newRow);
    }

}

function editCell(event){

    if(event.target.getElementsByTagName('img').length > 0){

        event.stopPropagation();

        var rowIndex = event.target.parentNode.rowIndex;
        rowIndex -= 1;
    var images = event.target.getElementsByTagName('img');
    var imageSource = images[0].src;
    var fileName = imageSource.substr(imageSource.lastIndexOf('/') + 1);
    if(fileName === "star2.png"){
      star(rowIndex);
      images[0].src = "resources/images/filled_star.png";

    }
    else{
      unStar(rowIndex);
      images[0].src = "resources/images/star2.png";
    }

    //alert(imageSource.substr(imageSource.lastIndexOf('/') + 1));
  }else if(event.target.tagName === 'IMG'){
    var cell = event.target.parentNode;
    event.stopPropagation();
      var rowIndex = event.target.parentNode.parentNode.rowIndex;
      console.log(rowIndex);
      var partNumber = event.target.parentNode.parentNode.childNodes[1].innerText;
      console.log(partNumber);
      rowIndex -= 1;
      var imageSource = event.target.src;
      var fileName = imageSource.substr(imageSource.lastIndexOf('/') + 1);
      if(fileName === "star2.png"){
      star(cell, rowIndex, partNumber);
      event.target.parentNode.innerHTML = "<svg class='spinner' width='20px' height='20px' viewBox='0 0 66 66' xmlns='http://www.w3.org/2000/svg'><circle class='circle-loader' fill='none' stroke-width='6' stroke-linecap='round' cx='33' cy='33' r='30'></circle></svg>";

    }
    else{
      unStar(cell, rowIndex, partNumber);
      event.target.parentNode.innerHTML = "<svg class='spinner' width='20px' height='20px' viewBox='0 0 66 66' xmlns='http://www.w3.org/2000/svg'><circle class='circle-loader' fill='none' stroke-width='6' stroke-linecap='round' cx='33' cy='33' r='30'></circle></svg>";
    }


  }
else{
        event.target.setAttribute('class', 'modal-trigger');
        event.target.setAttribute('href', '#modal1');


        var rowIndex = event.target.parentNode.rowIndex;
        var tableContainer = document.getElementById('table');
        var childNodes = tableContainer.children;
        var tableBody = childNodes[1];
        var rows = tableBody.children;

        console.log(rows);

        populateAndEditModal(rowIndex);


        var selectedRow = rows[rowIndex-1];
        var cell = selectedRow.childNodes[1];
        console.log(cell);

        partNumber = cell.innerText;
        // alert(partNumber);

        sessionStorage.partNumber = partNumber;

 }
}

function updateChart(json) {
            var partnumber = [];
            var quantityAvailable = [];
            var plannedVehicleQuantity = [];
            var dicv = [];
            for (var i = 0; i < json.length; i++) {
                if(i==4) break;
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

            var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                scaleFontColor: '#fffffff',
                data: {
                    labels: partnumber,
                    datasets: [{
                            label: "Quantity Avl",
                            backgroundColor: 'rgb(255, 99, 132)',
                            borderColor: 'rgb(255, 99, 132)',
                            data: quantityAvailable
                        },
                        {
                            label: "Planned Vehicle Qty",
                            backgroundColor: 'rgb(200, 200, 136)',
                            borderColor: 'rgb(200, 200, 136)',
                            data: plannedVehicleQuantity
                        }
                    ],
                },
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

function star(cell,rowIndex, partNumber){
  var url = "https://daimler-backend.herokuapp.com/api/current_user/starred_parts/";

  var formData = new FormData();

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

function unStar(cell,rowIndex, partNumber){

  var url = "https://daimler-backend.herokuapp.com/api/current_user/starred_parts/";

  var formData = new FormData();

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
    $('#part_name').text(shopType);
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





//get the values from the fields
var obj = {};

$('#done-btn').click(function(){
    obj['part_number'] = $('#part_number').val();
    obj['starred'] = $('#starred').val();
    obj['description'] = $('#description').val();
    obj['supplier_name'] = $('#supplier_name').val();
    obj['variants'] = $('#variants').val();
    obj['count'] = $('#count').val();
    obj['reported_on'] = $('#reported_on').val();
    obj['short_on'] = $('#short_on').val();
    obj['pmc'] = $('#pmc').val();
    obj['team'] = $('#team').val();
    obj['backlog'] = $('#backlog').val();
    obj['region'] = $('#region').val();
    obj['unloading_point'] = $('#unloading_point').val();
    obj['p_q'] = $('#p_q').val();
    obj['quantity'] = $('#quantity').val();
    obj['quantity_expected'] = $('#quantity_expected').val();
    obj['planned_vehicle_qty'] = $('#planned_vehicle_qty').val();
    obj['eta_dicv'] = $('#eta_dicv').val();
    obj['truck_details'] = $('#truck_details').val();
    obj['shortage_reason'] = $('#shortage_reason').val();
    obj['shop'] = $('#shop').val();

    // var warning = $('warning-radio-btn').isChecked();
    // var critical = $('critical-radio-btn').isChecked();
    // var normal = $('normal-radio-btn').isChecked();

    // if(warning === true)
    //     obj['status'] = 2;
    // if(critical === true)
    //     obj['status'] = 3;
    // if(normal === true)
    //     obj['status'] = 1;
    var status = $('input[name=status]:checked').next().text();
    if(status === "Warning")
        obj['status'] = 2;
    else if(status === 'Critical')
        obj['status'] = 3;
    else if(status === 'Normal')
        obj['status'] = 1;



    updateField(rowIndex, obj);
});


}

function updateField(rowIndex,obj){

console.log(JSON.stringify(obj));


  partNumber = json[rowIndex-1]['part_number'];
  console.log(partNumber);

  var url = "https://daimler-backend.herokuapp.com/api/parts/" + partNumber + "/";

  var xhr = new XMLHttpRequest();

// Open the connection.
xhr.open('PATCH', url, true);

xhr.setRequestHeader('Authorization','Token '+token);
xhr.setRequestHeader('Content-Type', 'application/json');

// Set up a handler for when the request finishes.
xhr.onload = function () {
  console.log(xhr.status);
  if (xhr.status === 200) {
    //alert('successful');
    location.reload(true);

  }
  else {
    alert('An error occurred!');
  }
};

// Send the Data.
xhr.send(JSON.stringify(obj));
}

function starSort(){

      var tableContainer = document.getElementById('table');
      var childNodes = tableContainer.children;
      console.log(childNodes);

      var tableBody = childNodes[1];
      var rows = tableBody.children;
      console.log(rows);

      //converting HTML collection to array.
      var rowsArray = Array.from(rows);

      //extracting index and image file path for each element
      var mapped = rowsArray.map(function(el, i) {
    return { index: i, value: el.childNodes[7].childNodes[0].src };
  });


      mapped.sort(function(a, b) {
      if (a.value > b.value) {
        return 1;
      }
      if (a.value < b.value) {
        return -1;
      }
      return 0;
});
      console.log(mapped);

      // container for the resulting order
    //   var result = mapped.map(function(el){
    //     return rowsArray[el.index];
    //   });
    // console.log(result);

// arranging the data according to the sorted values of HTMLcollection array.
      var jsonResponse = mapped.map(function(el){
        return json[el.index];
          });
        console.log(jsonResponse);
        updateDisplay(jsonResponse,date);

}





