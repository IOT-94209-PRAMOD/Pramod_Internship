import paho.mqtt.client as mqtt
from executeQuery import executeQuery

# Thresholds
PULSE_MIN = 60
PULSE_MAX = 100
SPO2_MIN = 95

pulse = None
spo2 = None

def on_message(client, userdata, message):
    global pulse, spo2

    value = int(message.payload.decode())

    if message.topic == "health/pulse":
        pulse = value
        print("Pulse:", pulse)

        if pulse < PULSE_MIN or pulse > PULSE_MAX:
            alert = f"ALERT! Abnormal Pulse Rate: {pulse}"
            client.publish("health/alert", alert)
            print(alert)

    elif message.topic == "health/spo2":
        spo2 = value
        print("SpO2:", spo2)

        if spo2 < SPO2_MIN:
            alert = f"ALERT! Low Blood Oxygen Level: {spo2}"
            client.publish("health/alert", alert)
            print(alert)

    # ✅ Insert ONLY when both values are received
    if pulse is not None and spo2 is not None:
        query = (
            f"INSERT INTO health_parameters (pulse, blood_oxygen) "
            f"VALUES ({pulse}, {spo2});"
        )
        executeQuery(query=query)

        print("Inserted into DB -> Pulse:", pulse, "SpO2:", spo2)

        pulse = None
        spo2 = None

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost", 1883)
subscriber.subscribe("health/#")

subscriber.loop_forever()
