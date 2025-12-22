import paho.mqtt.client as mqtt

# threshold values
PULSE_MIN = 60
PULSE_MAX = 100
SPO2_MIN = 95

def on_message(client, userdata, message):
    value = int(message.payload.decode())

    if message.topic == "health/pulse":
        print("Pulse:", value)

        if value < PULSE_MIN or value > PULSE_MAX:
            alert = f"ALERT! Abnormal Pulse Rate: {value}"
            client.publish("health/alert", alert)
            print(alert)

    elif message.topic == "health/spo2":
        print("SpO2:", value)

        if value < SPO2_MIN:
            alert = f"ALERT! Low Blood Oxygen Level: {value}%"
            client.publish("health/alert", alert)
            print(alert)

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost", 1883)
subscriber.subscribe("health/#")

subscriber.loop_forever()
