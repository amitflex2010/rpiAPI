const request = require("request");
const nodepixel = require('./neopixel-utils');
var gpio = require('onoff').Gpio;
var LED_SUCCESS = new gpio(4, 'out');
var LED_FAILURE = new gpio(6, 'out');
const url = "https://us-central1-mysampleproject-3b9ff.cloudfunctions.net/nodeapp/getContacts";

function checkEndpointStatus() {
  request.get(url, (error, response, body) => {
    if(body) {
      let json = JSON.parse(body);
    console.log(body);
      blinkSuccessLED(); 
    } if(error) {
      blinkFailureLED();
    }
    
  });
  
}

var pollEndpoint = setInterval(checkEndpointStatus, 5000);

function blinkSuccessLED() {
   /* if (LED_SUCCESS.readSync() === 0) {
      LED_SUCCESS.writeSync(1); //set output to 1 i.e turn led on
      } else {
        LED_SUCCESS.writeSync(0); //set output to 0 i.e. turn led off 
    
     } */

     var stripObj = nodepixel.Strip(7);
     console.log(stripObj.getPixelColor(4));
     stripObj.on('#ff0000');
     LED_SUCCESS.writeSync(stripObj);
  }

  function blinkFailureLED() {
    if (LED_FAILURE.readSync() === 0) {
      LED_FAILURE.writeSync(1); //set output to 1 i.e turn led on
      } else {
        LED_FAILURE.writeSync(0); //set output to 0 i.e. turn led off 
    
     } 
  }