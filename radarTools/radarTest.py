#!/usr/bin/python3

#
# Name  : radarTest.py
# Git   : git@gitpi:/home/git/gitProjects/piCamera.git
# Author: Patrick Conlon
# Date  : April, 6 2020
#
# Description: This is to test the RCWL-0516
# When motion is detected a timestamp will be
# displayed and the value returned. 
# 
# RASPBERRY PI PIN SETTING
# GPIO PIN 2  Power            -> 5V power
# GPIO PIN 4  Ground           -> Ground
# GPIO PIN 11 Signal Detection -> GPIO 17
#
# RCWL-0516 PIN SETTING
# PIN 2 GROUND
# PIN 3 OUT
# PIN 4 VIN
#
# SETUP
# RCWL-0516 -> RASPBERRY PI
# PIN 2     -> PIN 4
# PIN 3     -> PIN 11
# PIN 4     -> PIN 2
#

from gpiozero import DigitalInputDevice
from datetime import datetime
from signal   import pause

radar = DigitalInputDevice(17, pull_up=False, bounce_time=2.0)

def detector():
	now = datetime.now()
	activationTime = now.strftime("%Y.%m.%d_%H%M%S")
	print("Motion detected at " + activationTime)
	print("Value: " + str(radar.value))

print("Try to activate\n")
radar.when_activated = detector
pause()

