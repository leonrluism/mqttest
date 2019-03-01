 Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
pin = 25

# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
try:    
        # Ciclo principal infinito
        while True:
                # Obtiene la humedad y la temperatura desde el sensor 
                humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

                # Imprime en la consola las variables temperatura y humedad con un decimal
#               print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))
                print ('Sensor de Temperatura:' + str(temperatura))
                print ('Sensor de Humedad:' + str(humedad))


                ######################################################################
                #------------ CAMBIAR ID_MONGO POR VALOR CORRESPONDIENTE ------------#

                client.publish("sensor","LkTHoMzaFt7DgTQNd "+str(temperatura))
                client.publish("sensor","pGQDNmwswkQXfpp63 "+str(humedad))
               #########################################################################
       
       #Duerme 10 segundos
       time.sleep(2)
       
       Except Exception,e:
        print str(e)
