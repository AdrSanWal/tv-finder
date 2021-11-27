 $(document).ready(function(){
    $("#menu-toggle").click(function(e){
      e.preventDefault();
      $("#wrapper").toggleClass("menuDisplayed");
    });
  });

  function rangeInputChangeEventHandler(e){
    var rangeGroup = $(this).attr('name');
        minBtn = $(this).siblings('.min');
        maxBtn = $(this).siblings('.max');
        range_min = $(this).siblings('.range_min');
        range_max = $(this).siblings('.range_max');
        minVal = parseInt($(minBtn).val());
        maxVal = parseInt($(maxBtn).val());
        $(range_min).html(minVal);
        $(range_max).html(maxVal);
        
}

$('input[type="range"]').on( 'input', rangeInputChangeEventHandler);

$(function() {
    $(document).on('click', '#menu-toggle', function(event) {
        console.log('ok')
     });
   });