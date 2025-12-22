
# import required libraries
import paho.mqtt.client as mqtt
import random
import time

# create mqtt client
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# connect to mqtt broker
publisher.connect("localhost", 1883)

while True:
    intensity = random.randint(0, 100)            # LDR value
    temperature = round(random.uniform(20, 40), 2) # LM35 value

    # publish sensor data
    publisher.publish("sensor/ldr", intensity)
    publisher.publish("sensor/lm35", temperature)

    print(f"Published -> LDR: {intensity}, Temp: {temperature}")

    time.sleep(5)
