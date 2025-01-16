# Prueba de Keda para escalar un proyecto consumidor en función de métricas de Kafka

En este repo hay 4 elementos:

- Un script python que funciona como productor, enviando una cantidad configurable de mensajes
- Un container con un consumidor escrito en Python, que se conecta al cluster kafka y se registra en el tópico de prueba
- Una definición de un tópico de prueba que se puede usar en un cluster Openshift con el operador de AMQStreams instalado
- Una configuración de KEDA para el control del número de instancias del proyecto consumidor

Cada elemento tiene su README.md con algunas observaciones
