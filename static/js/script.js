$(document).ready(function(){
    $('.sidenav').sidenav({ edge: "right"});
    $("select").formSelect();
    // Disable selecting any date other then todays one for a input field posted date
    var dateToday = new Date();
    $("#posted_date").datepicker({
        minDate: dateToday,
        maxDate: dateToday,
        showClearBtn: true
    });
});
