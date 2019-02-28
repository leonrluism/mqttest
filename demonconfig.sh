#!/bin/bash
# Con openwrt debemos cambiar lo anterior por #!/bin/sh
# Configuración del broker y topic a escuchar.
# Cambiar por valores propios las siguientes variables:
archivo="/home/pi/salida.dat"
#-----------------------------------
#Conexion de base de datos
#mysql -u luis -p123456 <<MY_QUERY
#USE DOMOTICA
#SHOW tables
#MY_QUERY
user=luis
password=123456
#b='cocina'
#myvar=$(mysql DOMOTICA -u $user -p$password -se "select dht from config where espacio='$b'")
#------------------------------------
#Ponemos el cliente de mosquitto escuchando led cuarto
mosquitto_sub -t "casa/config" -h "wape.ddns.net" | while read value; do
# Guardamos valores uno detrás de otro:
echo "$value" >> $archivo

#Separamos el mensaje
#IN="sensor cocina led1 on"
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

#Validar si se va a agregar o eliminar
if [ $accion == "on" ]; then
	if echo "$nombre" | grep -q "led"; then
		#updetear la BB
		 upd=$(mysql DOMOTICA -u $user -p$password -se "update config set $nombre='on' where espacio='$espacio'")
	else
		#Consultar configuracion en la BD
		consul=$(mysql DOMOTICA -u $user -p$password -se "select $nombre from config where espacio='$espacio'")
		#AGREGAR EN EL CROTAB
		crontab -l > temp
		echo  $consul >> temp
		crontab temp
		rm temp
	fi
else
	 if echo "$nombre" | grep -q "led"; then
                #updetear la BD
		 upd=$(mysql DOMOTICA -u $user -p$password -se "update config set $nombre='off' where espacio='$espacio'")
        else
                #Consultar configuracion en la BD
                #consul=$(mysql DOMOTICA -u $user -p$password -se "select $nombreoff from config where espacio='$espacio'")
                #ELIMINAR EN EL CROTAB
		if [ $nombre == "dht" ]; then
			echo "hola"
			crontab -l | sed 's/\@reboot sleep 40\; python \/home\/pi\/mqttest\/'$espacio'\/dht11\/dht_consola.py/ /' | crontab -
		elif [ $nombre == "ldr" ]; then		
			crontab -l | sed 's/\@reboot sleep 40\; python \/home\/pi\/mqttest\/'$espacio'\/ldr\/sensorldr.py/ /'| crontab - $
		elif [ $nombre == "act1" ]; then         
			#CONFIGURAR ACTUADORES
                        crontab -l | sed 's/\@reboot sleep 40\; python \/home\/pi\/mqttest\/'$espacio'\/act\/sensorldr.py/ /'|$
                fi
	fi

fi

done
