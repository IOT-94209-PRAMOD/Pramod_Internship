import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

while True:
    pulse = random.randint(55, 120)        # simulate pulse
    spo2 = random.randint(88, 100)          # simulate blood oxygen

    client.publish("health/pulse", pulse)
    client.publish("health/spo2", spo2)

    print("Published -> Pulse:", pulse, "SpO2:", spo2)

    time.sleep(5)
