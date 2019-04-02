const request = require("request");
var gpio = require('onoff').Gpio;
var LED = new gpio(4, 'out');
const url = "https://us-central1-mysampleproject-3b9ff.cloudfunctions.net/nodeapp/getContacts";
request.get(url, (error, response, body) => {
  let json = JSON.parse(body);
  console.log(body);
blinkLED();
});

function blinkLED() {
    if (LED.readSync() === 0) {
        LED.writeSync(1); //set output to 1 i.e turn led on
      } else {
        LED.writeSync(0); //set output to 0 i.e. turn led off 
    
     } 
  }