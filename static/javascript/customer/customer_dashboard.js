/**
 * Created by Adam on 3/7/2017.
 */

// variables
var map;
var infowindow;
var geocoder;

//Map Helper Functions

// CONVERT ADDRESS TO LONG AND LAT
var addressToCoordinates = function addressToCoordinates (gecoder, address) {
    geocoder.geocode({'address': address}, function (results, status) {
        if (status == 'OK') {
            return results[0].geometry.location;
        }
    });
};

// SET MARKER AT GIVEN ADDRESS
var geocodeAddress = function geocodeAddress(geocoder, map, address) {
    geocoder.geocode({'address': address}, function (results, status) {
        if (status === 'OK') {
            setMarker(map, results[0].geometry.location);
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
};


// GET LOCATION
var successCallback = function (position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    setMarker(map, {lat: lat, lng: lng});
};

var errorCallback = function () {
    alert("Can't obtain current location :(");
};

function showCurrentLocation() {
    console.log("running getLocation()");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

// SET A MARKER
function setMarker(map, location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
    marker.setMap(map);
    map.panTo(marker.position);
    map.setZoom(12);
}

/*
    INITIALIZING MAP
 */
function initMap() {

    //Initialize Variables
    geocoder = new google.maps.Geocoder();
    infowindow = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 33.4169589, lng:-111.9377391}, //ASU Coordinates
        zoom: 10
    });

    // Display Starting Location on Map
    showCurrentLocation();
}


/*
    JAVASCRIPT FOR DASHBOARD PAGE - EXCLUDING MAPS JAVASCRIPT
 */

function showMarkerOnMap(button) {
    geocodeAddress(geocoder, map, button.value); //address is located in button value
}