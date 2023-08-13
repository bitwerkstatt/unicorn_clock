# Unicorn Berlin Clock
A little clock based on the berlin clock for a Raspi Pico and a Pimoroni unicorn LED display

# Usage
Place the main.py in the root directory of your Raspberry Pico (W). The clock will start once you power on the device.
It will be set to 00:00 initially, you can press the X button to get into the set time mode. Button A will then increase the hours,
button B the minutes. Once the time is set correctly, press X again to let the clock run.

# Berlin clock explained

The clock consists of for rows of LEDs. The upper row consists of four lamps (3 LEDs a lamp) with each lamp representing five hours that
have passed. The second row also has four lamps that represent one hour each. 

Example: Two lamps in the upper row => 10 hours have passed, one more in the second row => a single hour has also passed. Therefore we 
have 11 hours on our clock.

The third (blue) row shows eleven lamps (now one LED per lamp) with each representing 5 minutes passed, the fourth row  is four lamps again
for single minutes. Use the same counting and adding logic as for the hours.

Finally we have a blinking row in the middle (somewhat pinkish) that blinks in one second intervals.
