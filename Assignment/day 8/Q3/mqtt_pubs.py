import paho.mqtt.client as mqtt
import random
import time

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.connect("localhost", 1883)

while True:
    pulse = random.randint(55, 120)       
    spo2 = random.randint(90, 100)         

    publisher.publish("health/pulse", pulse)
    publisher.publish("health/spo2", spo2)

    print(f"Published -> Pulse: {pulse}, SpO2: {spo2}")

    time.sleep(2) 
    # publish every 2 seconds
