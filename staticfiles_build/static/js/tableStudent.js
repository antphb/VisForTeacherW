$(document).ready(function () {
    $("#example").DataTable();
});

var myLink = document.querySelector('a[href="#"]');
myLink.addEventListener("click", function (e) {
    e.preventDefault();
});

// requires jquery library
jQuery(document).ready(function() {
    jQuery(".main-table").clone(true).appendTo('#table-scroll').addClass('clone');   
});
 