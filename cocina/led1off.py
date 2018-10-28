#!/usr/bin/python
#autor: Jefferson Rivera
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
print "LED off"
GPIO.output(2,GPIO.LOW)


