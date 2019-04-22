pixel = require("node-pixel");
five = require("johnny-five");
var gpio = require('onoff').Gpio;

var LED_FAILURE = new gpio(6, 'out');

var board = new five.Board();
var strip = null;

board.on("ready", function() {
  // Define our hardware.
  // It's a 12px ring connected to pin 6.
  strip = new pixel.Strip({
    board: this,
    controller: "FIRMATA",
    strips: [ {pin: LED_FAILURE, length: 7}, ],
    gamma: 2.8,
  });

  // Just like DOM-ready for web developers.
  strip.on("ready", function() {
    // Set the entire strip to pink.
    strip.color('#903');

    // Send instructions to NeoPixel.
    strip.show();
  });

  // Allows for command-line experimentation!
  this.repl.inject({
    strip: strip
  });
});