(function() {
    function rangeInputChangeEventHandler(e){
        var rangeGroup = $(this).attr('name'),
            minBtn = $(this).parent().children('.min'),
            maxBtn = $(this).parent().children('.max'),
            range_min = $(this).parent().children('.range_min'),
            range_max = $(this).parent().children('.range_max'),
            minVal = parseInt($(minBtn).val()),
            maxVal = parseInt($(maxBtn).val())

        $(range_min).html(minVal);
        $(range_max).html(maxVal);
    }
 $('input[type="range"]').on( 'input', rangeInputChangeEventHandler);
})();

$(function() {$(document).on('click', '#menu-toggle', function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("menuDisplayed");
    });
});
console.log(Math.random())