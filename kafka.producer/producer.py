import os
import time
from datetime import datetime
from kafka import KafkaProducer
import json

# Variables de entorno para configuración
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "cluster-kafka-bootstrap-amq-streams-test.apps.ocptest.andreani.com.ar:443")
TOPIC_NAME = os.getenv("TOPIC_NAME", "infra.keda.autoscaler")
MESSAGE = os.getenv("MESSAGE", "Hola desde Python Producer!")  # Texto del mensaje
MESSAGE_COUNT = int(os.getenv("MESSAGE_COUNT", 1))  # Cantidad de instancias

def main():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        security_protocol="SSL",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")  # serialización a JSON
    )

    # Enviamos un lote de mensajes
    for i in range(MESSAGE_COUNT):
        # Fecha y hora en formato amigable
        friendly_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Marca de tiempo Unix
        unix_timestamp = int(time.time())

        # Crear el cuerpo del mensaje
        payload = {
            "index": i,
            "friendly_time": friendly_time,
            "unix_timestamp": unix_timestamp,
            "message_text": MESSAGE
        }

        # Se envía al tópico
        producer.send(TOPIC_NAME, value=payload)
        print(f"Enviando: {payload}")

        time.sleep(1)  # Pausa entre envíos (opcional)

    producer.flush()
    producer.close()
    print("Productor finalizado.")

if __name__ == "__main__":
    main()
