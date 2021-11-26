function filterTv(e, element) {
    let keynum;
    if(window.event) { // IE                  
        keynum = e.keyCode;
      } else if(e.which){ // Netscape/Firefox/Opera                 
        keynum = e.which;
      }
    alert(element.value + String.fromCharCode(keynum))
}

$("#menu-toggle").click(function(e) {
    alert('carga')
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
 });
 $("#menu-toggle-2").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled-2");
    $('#menu ul').hide();
 });
 
 function initMenu() {
    $('#menu ul').hide();
    $('#menu ul').children('.current').parent().show();
    //$('#menu ul:first').show();
    $('#menu li a').click(
       function() {
          var checkElement = $(this).next();
          if ((checkElement.is('ul')) && (checkElement.is(':visible'))) {
             return false;
          }
          if ((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
             $('#menu ul:visible').slideUp('normal');
             checkElement.slideDown('normal');
             return false;
          }
       }
    );
 }
 $(document).ready(function() {
    initMenu();
 });