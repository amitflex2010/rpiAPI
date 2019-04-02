const request = require("request");
var gpio = require('onoff').gpio;
var LED = new gpio(4, 'out');
const url = "https://us-central1-mysampleproject-3b9ff.cloudfunctions.net/nodeapp/getContacts";
request.get(url, (error, response, body) => {
  let json = JSON.parse(body);
  console.log(body);
  pio.write(7, true, function(err) {

    if (err) throw err;
    console.log('Written True to pin');
console.log(path.join(__dirname, 'public'));
blinkLED();
});
});

function blinkLED() {
 LED.writeSync(1); //set output to 1 i.e turn led on  
  }