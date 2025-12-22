import paho.mqtt.client as mqtt
import mysql.connector

# database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="smart_home",
    use_pure=True
)
cursor = db.cursor()

# default values
light_status = "OFF"
fan_status = "OFF"
temperature_value = 0.0

def on_message(client, userdata, message):
    global light_status, fan_status, temperature_value

    payload = message.payload.decode()

    if message.topic == "home/light":
        light_status = payload

    elif message.topic == "home/fan":
        fan_status = payload

    elif message.topic == "home/temp":
        temperature_value = float(payload)

    # insert into SAME table
    sql = """
    INSERT INTO appliance_status (light, fan, temperature)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (light_status, fan_status, temperature_value))
    db.commit()

    print("Inserted:", light_status, fan_status, temperature_value)

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost", 1883)
subscriber.subscribe("home/#")

subscriber.loop_forever()
