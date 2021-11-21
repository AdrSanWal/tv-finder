function filterTv(e, element) {
    let keynum;
    if(window.event) { // IE                  
        keynum = e.keyCode;
      } else if(e.which){ // Netscape/Firefox/Opera                 
        keynum = e.which;
      }
    alert(element.value + String.fromCharCode(keynum))
}
