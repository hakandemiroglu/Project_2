var API_KEY = "pk.eyJ1IjoibWVyeWVtbWxrIiwiYSI6ImNqcHVkanVhbjBmcTM0M282MmowcnJlZ3AifQ.jpDXpNPhKT8vC9vCj6-UrQ";

var map = L.map("map", {
  center: [33.767693,-84.4908152],
  zoom: 12
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(map);



// Grabbing our GeoJSON data..
d3.json("outfile.json", function(response) {
 console.log(response)
  // Create a new marker cluster group
  //var markers = L.markerClusterGroup();

  // Loop through data
  for (var i = 0; i < response.length; i++) {

    // Set the data location property to a variable
    var location = response[i].geometry;

    // Check for location property
    if (location) {

      // Add a new marker to the cluster group and bind a pop-up
     str = ""
      for (var j = 0; j < response[i].value.length ; j++)   {
          str = str + "<h2>" + response[i].value[j].display_name + ":"+ response[i].value[j].estimate + "</h2> <hr>"
      }  
      //  console.log(response[i].value.length)
      L.marker([location[0], location[1]])
        .bindPopup("<h1>" + response[i].place +"</h1> <hr>" + str ).addTo(map);
    }

  }

  // Add our marker cluster layer to the map
  //myMap.addLayer(markers);

});
