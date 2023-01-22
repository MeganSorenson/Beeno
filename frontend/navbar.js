$( document ).ready(function() {
    console.log( "ready!" );
    $("#navbar").addClass("navbar navbar-light bg-light")
    $("#navbar").append('<a href="/pages/booking.html">Home</a>')
    $("#navbar").append('<a href="/pages/my_parking_stalls.html">Reservations</a>')
    $("#navbar").append('<a href="/pages/add_parking.html">Offerings</a>')
    $("#navbar").append('<a href="/index.html">Logout</a>').append(<span class="material-icons">&#xE87C;</span>)
});