#!/usr/bin/python
#autor: Jefferson Rivera
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
print "LED off"
GPIO.output(4,GPIO.LOW)


