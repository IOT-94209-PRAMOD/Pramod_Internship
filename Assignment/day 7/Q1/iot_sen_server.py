from flask import Flask, request
from datetime import datetime as dt

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a Flask server
server = Flask(__name__)


@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"


# CREATE (Insert sensor data)
@server.post('/iot_sen')
def create_sensor():
    # extract data from form
    id = request.form.get('id')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')

    # create insert query (explicit column names)
    query = f"""
        INSERT INTO sen_readings (id, temperature, humidity,timesamp)
        VALUES ({id}, {temperature}, {humidity}, '{dt.now()}');
    """

    executeQuery(query=query)

    return "sensor_data added successfully"


# READ (Retrieve sensor data)
@server.get('/iot_sen')
def retrieve_sensors():
    query = "SELECT * FROM sen_readings;"
    data = executeSelectQuery(query=query)

    return {"sen_readings": data}


# UPDATE (Update humidity)
@server.put('/iot_sen')
def update_sensor():
    sensor_id = request.form.get('id')
    humidity = request.form.get('humidity')

    query = f"""
        UPDATE sen_readings
        SET humidity = {humidity}
        WHERE id = {sensor_id};
    """

    executeQuery(query=query)

    return "humidity updated successfully"


# DELETE (Delete by temperature)
@server.delete('/iot_sen')
def delete_sensor():
    temperature = request.form.get('temperature')

    query = f"""
        DELETE FROM sen_readings
        WHERE temperature = {temperature};
    """

    executeQuery(query=query)

    return "sensor_data deleted successfully"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
