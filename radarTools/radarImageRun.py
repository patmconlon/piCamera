#!/usr/bin/python3

#
# Name:   radarImageRun.py
# Git:    git@gitpi:/home/git/gitProjects/piCamera.git
# Author: Patrick Conlon
# Date:   April, 6 2020
#
# Description: This is to use the RCWL-0516
# When motion is detected the hostname and timestamp will be
# used as the filename. The image will have a banner of
# blue and yellow that shows the date and time as well as
# the hostname.
# The hostname is important for multiple cameras uploading
# to the same location.
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
from picamera import PiCamera, Color
from signal   import pause
import socket

cameraHeight               = 1024
cameraWidth                = 768
radar                      = DigitalInputDevice(17, pull_up=False, bounce_time=2.0)
camera                     = PiCamera()
hostname                   = socket.gethostname() 
camera.resolution          = (1024, 768)
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')

def motionDetection():
	now = datetime.now()
	pictureTime = now.strftime("%Y.%m.%d_%H%M%S")
	camera.annotate_text = hostname + ": " + pictureTime
	camera.capture('/media/web/radarPI/' + hostname + "." + pictureTime + ".jpg")

while True:
	radar.when_activated = motionDetection
	pause()

