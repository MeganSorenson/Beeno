$(document).ready(function () {
    console.log("ready!");
    $("#navbar").addClass("navbar navbar-light bg-light")
    $("#navbar").append('<a href="/">login</a>')
    $("#navbar").append('<a href="/pages/my_parking_stalls.html">My Parking Stalls</a>')
    $("#navbar").append('<a href="/">logout</a>')
});