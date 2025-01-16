import os
import sys
import signal
import time
from kafka import KafkaConsumer

# Variables de entorno para configuración
# Ajusta según tu caso o carga desde ConfigMap/Secret en OpenShift:
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "help!")
TOPIC_NAME = os.getenv("TOPIC_NAME", "help!")

# Control de la señal para un cierre limpio
exit_event = False
def handle_sigterm(signum, frame):
    global exit_event
    exit_event = True

signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGINT, handle_sigterm)

def get_consumer():
    """
    Crea y devuelve un KafkaConsumer conectado a AMQ Streams.
    Ajusta la configuración de SSL / SASL si es necesario.
    """
    consumer_config = {
        "bootstrap_servers": BOOTSTRAP_SERVERS.split(","),
        "group_id": "keda-autoscaler-consumer",
        "auto_offset_reset": "earliest", 
        "enable_auto_commit": True,
        "security_protocol": "SSL"
    }

    return KafkaConsumer(TOPIC_NAME, **consumer_config)

def main():
    if BOOTSTRAP_SERVERS == "help!" or TOPIC_NAME == "help!":
        print("Por favor, configura las variables de entorno BOOTSTRAP_SERVERS y TOPIC_NAME", file=sys.stderr)
        sys.exit(1)

    consumer = get_consumer()
    print(f"Consumidor conectado a {BOOTSTRAP_SERVERS}, escuchando tópico '{TOPIC_NAME}'")

    # Bucle principal
    try:
        while not exit_event:
            # poll(…) o consumer.poll(…) en otras librerías
            for message in consumer:
                # “Destruir” el mensaje: 
                # En la práctica podrías hacer algo más útil,
                # pero aquí simplemente lo descartamos.
                # Log opcional para ver que algo pasa:
                print(f"Mensaje consumido: offset={message.offset}, payload={message.value}")

                if exit_event:
                    break
            time.sleep(1)

    except Exception as e:
        print(f"Ocurrió un error en el consumo: {e}", file=sys.stderr)
    finally:
        consumer.close()
        print("Cerrando consumidor...")

if __name__ == "__main__":
    main()
