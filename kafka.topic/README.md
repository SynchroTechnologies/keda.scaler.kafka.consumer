# Topico de prueba en Kafa

## Objetivo

Probar KEDA detectando eventos en colas de Kafka para escalar un consumidor.

### Creación del tópico en el cluster Kafka

Asumimos un ambiente OpenShift, con el operador de AMQStreams instalado y un cluster desplegado y funcionando.

El tópico es simple, las aplicaciones de producción y consumo de mensajes usan un esquema Json simple, con una seralización por defecto, no se involucra API Curio en ésta prueba.

Se elije crear 10 particiones para el tópico, con el fin de crear hasta 10 instancias del consumidor, y que KEDA juegue escalando / desescalando en el rango de 1 a 10 instancias en el proyecto consumidor.