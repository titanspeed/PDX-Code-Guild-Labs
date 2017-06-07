'use strict';

var x = document.getElementById("bustext");
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
} else {
    x.innerHTML = "Geolocation is not supported by this browser.";
}

var lat;
var lon;
var resultset;

function showPosition(position) {
    lat = position.coords.latitude;
    lon = position.coords.longitude;
    x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
    $.ajax({
        url: "https://developer.trimet.org/ws/V1/stops",
        type: "GET",
        data: {
            'APPID': '9D3D03025E095BA2703409068',
            'll': lat + ',' + lon,
            'meters': 500,
            'json': true
        },
        success: function (d) {
            resultset = d.resultSet.location;
            console.log(d);
            console.log(lat + ',' + lon);
            var html = '';
            resultset.forEach(function (i, x) {
                html += d.resultSet.location[x].desc + '<br>';
            });

            $('.stops').html(html);


        },
        error: function () {
            console.log(d);
        }
    });
}

