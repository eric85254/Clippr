/**
 * Created by adaml on 2/10/2017.
 */


    // This example requires the Places library. Include the libraries=places
    // parameter when you first load the API. For example:
    // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
    //ToDo: the map needs some database love
var map;
var infowindow;

function initMap() {
    var pyrmont = {lat: 33.425, lng: -111.923};

    map = new google.maps.Map(document.getElementById('map'), {
        center: pyrmont,
        zoom: 15
    });

    infowindow = new google.maps.InfoWindow();
    var marker = new google.maps.Marker({
        position: pyrmont,
        map: map,
        title: 'Hello World!'
    });
    marker.setMap(map);

    var geocoder = new google.maps.Geocoder();
    address = '1050 S. Stanley Pl';
    geocodeAddress(geocoder, map, address)
}

geocodeAddress = function geocodeAddress(geocoder, resultsMap, address) {
    geocoder.geocode({'address': address}, function (results, status) {
        if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: resultsMap,
                position: results[0].geometry.location
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
};

// function callback(results, status) {
//     if (status === google.maps.places.PlacesServiceStatus.OK) {
//         for (var i = 0; i < results.length; i++) {
//             createMarker(results[i]);
//         }
//     }
// }
//
// function createMarker(place) {
//     var placeLoc = place.geometry.location;
//     var marker = new google.maps.Marker({
//         map: map,
//         position: place.geometry.location
//     });
//
//     google.maps.event.addListener(marker, 'click', function () {
//         infowindow.setContent(place.name);
//         infowindow.open(map, this);
//     });
// }