#!/usr/bin/python
#autor: Jefferson Rivera
#import sys
#import signal
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
print "LED on"
GPIO.output(17,GPIO.HIGH)
