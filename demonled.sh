#!/bin/bash
# Con openwrt debemos cambiar lo anterior por #!/bin/sh
# Configuración del broker y topic a escuchar.
# Cambiar por valores propios las siguientes variables:
archivo="/home/pi/salida.dat"
#-----------------------------------
#Conexion de base de datos
user=luis
password=123456
#------------------------------------
#Ponemos el cliente de mosquitto escuchando led cuarto
mosquitto_sub -t "casa/leds" -h "wape.ddns.net" | while read value; do
# Guardamos valores uno detrás de otro:
echo "$value" >> $archivo

#Separamos el mensaje
#value="cocina led1 off"
arrIN=(${value//' '/ })
cont=0

#Separar mensaje
for i in "${arrIN[@]}"
do
	if (($cont==0)); then
		espacio=$i
	elif (($cont==1)); then
		nombre=$i
	elif (($cont==2)); then
		accion=$i
	fi

	cont=$cont+1
done

#Validar si se va a encender o apagar
if [ $accion == "on" ]; then
	cd /home/pi/mqttest/$espacio
	n="$nombre""on.py"
	chmod 777 $n
	./$n
else
	cd /home/pi/mqttest/$espacio
        n="$nombre""off.py"
        chmod 777 $n
        ./$n
fi


