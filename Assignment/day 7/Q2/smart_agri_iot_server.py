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
@server.post('/smart_agri_iot')
def create_sensor():
    # extract data from form
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')
  

    # create insert query (explicit column names)
    query = f"""
        INSERT INTO smart_agri_iot (sensor_id, moisture_level,date_and_time)
        VALUES ({sensor_id}, {moisture_level}, '{dt.now()}');
    """

    executeQuery(query=query)

    return "sensor_data added successfully"


# READ (Retrieve sensor data)
@server.get('/smart_agri_iot')
def retrieve_sensors():
    query = "SELECT * FROM smart_agri_iot;"
    data = executeSelectQuery(query=query)

    return {"smart_agri_iot": data}


# UPDATE (Update humidity)
@server.put('/smart_agri_iot')
def update_sensor():
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')

    query = f"""
        UPDATE smart_agri_iot
        SET moisture_level = {moisture_level}
        WHERE sensor_id = {sensor_id};
    """

    executeQuery(query=query)

    return "moisture_level updated successfully"


# DELETE (Delete by temperature)
@server.delete('/smart_agri_iot')
def delete_sensor():
    sensor_id = request.form.get('sensor_id')

    query = f"""
        DELETE FROM smart_agri_iot
        WHERE sensor_id = {sensor_id};
    """

    executeQuery(query=query)

    return "sensor_data deleted successfully"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
