# Consumidor de Kafka en python

## Objetivo

Probar KEDA detectando eventos en colas de Kafka para escalar un consumidor.

### Build de la aplicación

Las librearías de "kafka-python" funcionan bien con Python <= 3.11

En python >= 3.12 tienen un error de dependencia.

### Run de la aplicación

Se puede correr a mano el script en un ambiente Python <= 3.11, si está instalado Python correctamente

El productor (y el consumidor también) depende de dos librearías Python que deben estar instaladas:

- kafka-Python, se puede instalar con pip o si el sistema tiene un package manager, en un ambiente python virtual:

  - pip install kafka-python six
  - apk install python3-kafka python3-six    (para Ubuntu o Debian)

Si no hay un ambiente Python instalado, se puede buildear una imagen docker a partir del Dockerfile y correr el container para ejecutar el productor

El productor necesita las siguientes variables de entorno:

- BOOTSTRAP_SERVERS  colocar el FQDN o dirección IP del servicio Bootsrap de Kafka
- TOPIC_NAME   es el nómbre que tiene el tópico en el cluster Kafka
- MESSAGE   un mensaje de texto arbitrario, para incluir en el payload del mensaje
- MESSAGE_COUNT   Cantidad de mensajes a ser generados y enviados a Kafka, por defecto, 1 mensaje
