$(document).ready(function () {
    console.log("ready!");
    $("#navbar").addClass("navbar navbar-light bg-light")
    $("#navbar").append('<a href="/pages/booking.html">Book A Stall</a>')
    $("#navbar").append('<a href="/pages/my_parking_stalls.html">My Bookings</a>')
    $("#navbar").append('<a href="/pages/add_parking.html">My Parking</a>')
    $("#navbar").append('<a href="/">Logout</a>')
});