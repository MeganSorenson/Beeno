mapboxgl.accessToken = 'pk.eyJ1IjoiZXJpY3BpZW4iLCJhIjoiY2xkN2x3OWJqMW52azNucGF2MDhnZDM4eCJ9.6Os86rNwkmy35WNtZqpsZw';

const monument = [-77.0353, 38.8895];

const map = new mapboxgl.Map({
    container: 'map', // container ID
    // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    style: 'mapbox://styles/mapbox/streets-v12', // style URL
    zoom: 0 // starting zoom
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

