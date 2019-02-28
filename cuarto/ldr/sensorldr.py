
#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import commands
import paho.mqtt.client as mqtt


#connect to client
client =mqtt.Client("ldr")

#############################
#--.CAMBIAR IP POR VALOR CORRESPONDIENTE--

client.connect("wape.ddns.net")

################################

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#define the pin that goes to the circuit
pin_to_circuit = 16

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    apagado=0	
    while True:
	ldr= rc_time(pin_to_circuit)
	print (ldr)
	#######################################
	#----CAMBIAR  ID_MONGO ----------------
	client.publish("sensor","id_mongo_ldr "+str(ldr))

	#######################################
      	''' ldr= rc_time(pin_to_circuit)
	if ldr>1000:
		print ("Encender luces")
		apagado=1
		commands.getoutput('/usr/bin/python /home/pi/mqttest/led/ledcuartoon.py')
	else:
		if apagado==1:
			print ("Apagar luces")
			commands.getoutput('/usr/bin/python /home/pi/mqttest/led/ledcuartooff.py')
			apagado=0'''
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
