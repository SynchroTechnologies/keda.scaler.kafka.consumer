# Consumidor de Kafka en python

## Objetivo

Probar KEDA detectando eventos en colas de Kafka para escalar un consumidor.

### Build de la aplicación

Las librearías de "kafka-python" funcionan bien con Python <= 3.11

En python >= 3.12 tienen un error de dependencia.

### Run de la aplicación

Solo hace falta un manifiesto de "Deployment". No hay ni servicios, ni rutase.

Los mensajes consumidos se pueden leer en el log del container

Para ejecutar la aplicación hacen falta 2 (dos) variables de entorno:

- BOOTSTRAP_SERVERS  colocar el FQDN o dirección IP del servicio Bootsrap de Kafka
- TOPIC_NAME   es el nómbre que tiene el tópico en el cluster Kafka

