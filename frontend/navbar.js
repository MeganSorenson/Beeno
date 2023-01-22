$( document ).ready(function() {
    console.log( "ready!" );
    $("#navbar").addClass("navbar navbar-light bg-light")
    $("#navbar").append('<a href="/frontend/">login</a>')
    $("#navbar").append('<a href="/frontend/my_parking_stalls.html">My Parking Stalls</a>')
    $("#navbar").append('<a href="/frontend/">logout</a>')
});