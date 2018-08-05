#!/bin/bash
# Con openwrt debemos cambiar lo anterior por #!/bin/sh
# Configuración del broker y topic a escuchar.
# Cambiar por valores propios las siguientes variables:
#------------------------------------
#Ponemos el cliente de mosquitto escuchando led cuarto
mosquitto_sub -t "led/cocina" -h "192.168.0.107" | while read value; do
# Guardamos valores uno detrás de otro:
	echo "$value"
	if [ "$value" == "ledcocinaon" ]; then
		cd /home/pi/mqttest/led
		chmod 777 ledcocinaon.py
		./ledcocinaon.py
	else
		cd /home/pi/mqttest/led
		chmod 777 ledcocinaoff.py
		./ledcocinaoff.py
	fi
#echo "$value" >> $archivo

done

mosquitto_sub -t "led/sala" -h "192.168.0.107" | while read value; do
        echo "$value"

done
