import paho.mqtt.client as mqtt
import time
import random

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.connect("localhost", 1883)

while True:
    publisher.publish("home/light", "ON")
    publisher.publish("home/fan", "OFF")
    publisher.publish("home/temp", round(random.uniform(25, 40), 2))
    print("Light ON | Fan OFF | Temp sent")
    time.sleep(10)

    publisher.publish("home/light", "OFF")
    publisher.publish("home/fan", "ON")
    publisher.publish("home/temp", round(random.uniform(25, 40), 2))
    print("Light OFF | Fan ON | Temp sent")
    time.sleep(10)
