/**
 * MYCLIENT.JS
 * an example of a JSON request - an ajax request which returns a JSON object 
 * 
 * When a user browses to http://localhost:3000, index.html is loaded, which then 
 * loads and executes this code
 */

window.onload = function () {
    var url, i;
  
   // for (i = 0; i < 2; i++) {
      url = "https://us-central1-mysampleproject-3b9ff.cloudfunctions.net/nodeapp/getContacts" //document.URL + 'inputs/' + i;
      $.getJSON(url, function (data) {
        console.log('API response received');
        console.log(data);
       // $('#input').append('<p>input gpio port ' + data.gpio + ' on pin ' + data.pin + ' has current value ' + data.value + '</p>');
      });
    //}
  };