import RPi.GPIO as GPIO
import time
import threading

#GPIO.setmode(GPIO.BOARD)



class Conexion4(threading.Thread):
 

   def __init__(self, cb):
	threading.Thread.__init__(self)
        self.callback = cb
        self.pin_to_circuit=7
	self.count=0

   def run(self):
	print "hola"
   
  
	#Output on the pin for 
	GPIO.setup(self.pin_to_circuit, GPIO.OUT)
	GPIO.output(self.pin_to_circuit, GPIO.LOW)
	time.sleep(0.1)
    
	GPIO.setup(11, GPIO.OUT)
    

    #Change the pin back to input
    	GPIO.setup(self.pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    	while (GPIO.input(self.pin_to_circuit) == GPIO.LOW):
        	self.count += 1
 
		self.callback=self.count
		return self.callback

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    """while True:
        if run(self)>2000:
            print 'prende'
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW)"""
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
