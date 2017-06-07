'use strict';


var x = document.getElementById("weathertext");
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
} else {
    x.innerHTML = "Geolocation is not supported by this browser.";
}

var lat;
var lon;

function showPosition(position) {
    lat = position.coords.latitude;
    lon = position.coords.longitude;
    x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        type: "GET",
        data: {
            'APPID': 'c8eac569cc2d3fdfcacf8e3d12ab728f',
            'units': 'imperial',
            'lat': lat,
            'lon': lon
        },
        success: function (d) {
            console.log(d);
            var desc = d.weather[0].description;
            var temp = d.main.temp;
            var nam = d.name;

            $('#weather').html(d.name + ' ' + d.main.temp + ' ' + d.weather[0].description);
            if (desc === 'clear sky') {
                $('#represent').attr('src', 'sun.jpg')
            } else if (desc === 'broken clouds') {
                $('#represent').attr('src', 'sun.jpg')
            } else if (desc === 'rain'){
                $('#represent').attr('src', 'rain.png')
            } else if (desc === 'broken clouds') {
                $('#represent').attr('src', 'cloudy.jpg')
            }
        },
        error: function (d) {
            console.log(d);
        }
    });
}
