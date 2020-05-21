#!/usr/bin/python3

#
# Name:   radarMotionRun.py
# Git:    git@gitpi:/home/git/gitProjects/piCamera.git
# Author: Patrick Conlon
# Date:   April, 11 2020
#
# Description: This is to record from the RCWL-0516
# When motion is detected the hostname and timestamp will be
# used as the filename to record the 10 seconds of video.
# This process will continue as each instance of movement
# is detected.
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
from picamera import PiCamera
from signal   import pause
from time     import sleep
import socket

radar             = DigitalInputDevice(17, pull_up=False, bounce_time=12.0)
camera            = PiCamera()
hostname          = socket.gethostname()
camera.resolution = (1024, 768)

def motionDetection():
	now         = datetime.now()
	pictureTime = now.strftime("%Y.%m.%d_%H%M%S")

	camera.start_preview()
	camera.start_recording('/media/web/radarPI/' + hostname + "." + pictureTime + ".h264")
	sleep(10)
	camera.stop_recording()
	camera.stop_preview()

while True:
	radar.when_activated = motionDetection
	pause()

