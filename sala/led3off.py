#!/usr/bin/python
#autor: Jefferson Rivera
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(9,GPIO.OUT)
print "LED off"
GPIO.output(9,GPIO.LOW)


