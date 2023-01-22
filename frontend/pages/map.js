mapboxgl.accessToken = 'pk.eyJ1IjoiZXJpY3BpZW4iLCJhIjoiY2xkN2x3OWJqMW52azNucGF2MDhnZDM4eCJ9.6Os86rNwkmy35WNtZqpsZw';

const monument = [-77.0353, 38.8895];

const map = new mapboxgl.Map({
    container: 'map', // container ID
    // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    style: 'mapbox://styles/mapbox/streets-v12', // style URL
    center: monument, // starting position [lng, lat]
    zoom: 15 // starting zoom
});

const popup = new mapboxgl.Popup({ offset: 25 }).setText(
    'Construction on the Washington Monument began in 1848.<a href=google.com>test</a>'
);
     
// create DOM element for the marker
const el = document.createElement('div');
el.id = 'marker';
    
// create the marker
new mapboxgl.Marker(el)
.setLngLat(monument)
.setPopup(popup) // sets a popup on this marker
.addTo(map)


function getBookings() {
    console.log("test");

    let date = document.getElementById("date").value;
    let place = document.getElementById("locations").value;


    let url = `http://127.0.0.1:1999/park?type=all&place=${place}&date=${date}`;

    fetch(url)
        .then(response => {
            return response.json();
        })
        .then(json => {
            console.log(json);
            let container = document.getElementById("available_stalls");
            for (const parking_id in json) {
                let tr = document.createElement("tr");

                let latTd = document.createElement("td");
                latTd.innerText = json[parking_id].lat
                tr.appendChild(latTd);

                container.appendChild(tr);
            }
        })
        .catch(error => {
            console.log(error);
        });
}
