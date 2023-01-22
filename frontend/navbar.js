$( document ).ready(function() {
    console.log( "ready!" );
    $("#navbar").addClass("navbar navbar-light bg-light")
    $("#navbar").append('<a href="/frontend/pages/booking.html">Home</a>')
    $("#navbar").append('<a href="/frontend/pages/my_parking_stalls.html">Reservations</a>')
    $("#navbar").append('<a href="/frontend/pages/add_parking.html">Offerings</a>')
    $("#navbar").append('<a href="/frontend/index.html">Logout</a>')
});