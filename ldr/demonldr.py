#!/usr/bin/python
#autor: Jefferson Rivera
import sys
import signal
from gpiozero import LED
from clases.Conexioncuarto import Conexion
from clases.Conexionsala import Conexion2
from clases.Conexioncocina import Conexion3
from clases.ldrtest import Conexion4


ledcuarto = LED(4)
ledsala=  LED (17)
ledcocina= LED (14)

#LED CUARTO
def procesa(respuesta):
    print respuesta

    if respuesta:
    	ledcuarto.on()
    	print "Encendido cuarto"
    else:
    	ledcuarto.off()
    	print "Apagado cuarto"
    sys.stdout.flush()

#LED SALA
def procesasala(respuesta2):
    print respuesta2

    if respuesta2:
    	ledsala.on()
    	print "Encendido sala"
    else:
    	ledsala.off()
    	print "Apagado sala"
    sys.stdout.flush()
    
#LED COCINA
def procesacocina(respuesta3):
    print respuesta3

    if respuesta3:
    	ledcocina.on()
    	print "Encendido cocina"
    else:
    	ledcocina.off()
    	print "Apagado cocina"
    sys.stdout.flush()    

#LDR
def procesaldr(respuesta4):
    print respuesta4

    """if respuesta3:
    	ledcocina.on()
    	print "Encendido cocina"
    else:
    	ledcocina.off()
    	print "Apagado cocina"""
    sys.stdout.flush()   


try:
	print "Inicio"
	t = Conexion(procesa)
	t.daemon=True
	t.start()
	t2 = Conexion2(procesasala)
	t2.daemon=True
	t2.start()
	t3 = Conexion3(procesacocina)
	t3.daemon=True
	t3.start()
	t4 = Conexion4(procesaldr)
	t4.daemon=True
	t4.start()
	"""t5 = Conexion(procesasala)
	t5.daemon=True
	t5.start()
	t6 = Conexion(procesasala)
	t6.daemon=True
	t6.start()"""
	signal.pause()
except (KeyboardInterrupt, SystemExit):
	raise
	print "Salida"
