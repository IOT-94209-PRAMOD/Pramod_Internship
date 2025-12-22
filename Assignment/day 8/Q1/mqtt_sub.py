import paho.mqtt.client as mqtt
import mysql.connector

# database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_home"
)

cursor = db.cursor()

def on_message(client, userdata, message):
    print("Topic:", message.topic)
    print("Payload:", message.payload)

    value = float(message.payload.decode())

    if message.topic == "sensor/ldr":
        sensor = "LDR"
    elif message.topic == "sensor/lm35":
        sensor = "LM35"
    else:
        return

    sql = "INSERT INTO sensor_data (sensor_type, value) VALUES (%s, %s)"
    cursor.execute(sql, (sensor, value))
    db.commit()

    print(f"Inserted -> {sensor}: {value}")

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost", 1883)
subscriber.subscribe("sensor/ldr")
subscriber.subscribe("sensor/lm35")

subscriber.loop_forever()
