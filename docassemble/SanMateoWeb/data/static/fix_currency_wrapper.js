$(document).on('daPageLoad', function(){
  var currencywrappers = document.getElementsByClassName("da-embed-currency-wrapper");
  for (var i=0; i < currencywrappers.length; i++) {
    currencywrappers[i].style.width = "180px";
  }
});