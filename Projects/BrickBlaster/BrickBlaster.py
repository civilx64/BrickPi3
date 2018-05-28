#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2017 civilx64 
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code controls a blaster that is fired by an axle spinning horizontally
# under a magazine of 3x beams. 
# 
# Hardware: Connect an EV3 or NXT touch sensor to BrickPi3 Port 1.
# Connect an EV3 or NXT motor to BrickPi3 Port A.
# 
# Results: The blaster will fire while the touch sensor is pressed. 
#

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BRICKBLASTER_VERSION = "0.1.0"

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# Configure for a touch sensor.
# If an EV3 touch sensor is connected, it will be configured for EV3 touch, otherwise it's configured for NXT touch.
# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# BP.SENSOR_TYPE.TOUCH specifies that the sensor will be a touch sensor.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.NXT_TOUCH)

try:
    while True:
        # Await firing instructions.
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns the sensor value.
        # A value of 1 means the sensor is pressed and the blaster should fire.
        # A value of 0 means the sensor is not pressed and the blaster should not fire.
        try:
            value = BP.get_sensor(BP.PORT_1)
            if (value == 1):
                BP.set_motor_power(BP.PORT_A, -50)
                print("FIRE!")
            if (value == 0):
                BP.set_motor_power(BP.PORT_A, 0)
                print("Blaster armed - press trigger to fire.")
	
        except brickpi3.SensorError as error:
            print(error)
        
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
    print("***********************************")
    print("Safety on. Ready to reload.")
    print("********BrickBlaster v{}********".format(BRICKBLASTER_VERSION))

