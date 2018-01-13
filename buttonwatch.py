#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Import the custom 'turret' library
import turret

# Set up the GPIO pins (BCM)
ledPin = 22
buttonPin = 24

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Setup the button
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Light the LED to indicate the program is ready
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, True)

# Start the turret library
turret.init()

# Start a loop...
while True:
	# Get the button state - pushed or not?
    input_state = GPIO.input(buttonPin)
    # If button is pushed...
    if input_state == False:
    	# Fire the cannon!
        turret.fire()
        # Sleep to make sure no duplicate function calls
        time.sleep(3)