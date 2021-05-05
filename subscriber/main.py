import json
import os

import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc, properties=None):
    print("Connected with result code " + str(rc))
    client.subscribe("chatter")


def on_message(client, userdata, message):
    print(message.topic)
    msg_json = message.payload.decode()
    data = json.loads(msg_json)
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)


if __name__ == "__main__":
    client = mqtt.Client()
    client.username_pw_set(
        username=os.getenv("VERNEMQ_USER"), password=os.getenv("VERNEMQ_PASSWORD")
    )

    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect("mqtt_broker", 1883, 60)
    except ConnectionRefusedError as e:
        print(
            "First attempt to connect fails because the docker container for the MQTT server needs to start."
        )
        print(e)

    client.loop_forever()
