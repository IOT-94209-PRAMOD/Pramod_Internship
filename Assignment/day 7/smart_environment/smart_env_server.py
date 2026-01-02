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
@server.post('/environment')
def create_sensor():
    # extract data from form
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    gas_level = request.form.get('gas_level')
  

    # create insert query (explicit column names)
    query = f"""
        INSERT INTO env_data (temperature, humidity, gas_level, date_and_time)
        VALUES ({temperature}, {humidity}, {gas_level}, '{dt.now()}');
    """

    executeQuery(query=query)

    return "sensor_data added successfully"


# READ (Retrieve sensor data)
@server.get('/environment')
def retrieve_sensors():
    query = "SELECT * FROM env_data;"
    data = executeSelectQuery(query=query)

    return {"env_data": data}


# UPDATE (Update humidity)
@server.put('/environment')
def update_sensor():
    id = request.form.get('id')
    humidity = request.form.get('humidity')

    query = f"""
        UPDATE env_data
        SET humidity = {humidity}
        WHERE id = {id};
    """

    executeQuery(query=query)

    return "humidity updated successfully"


# DELETE (Delete by temperature)
@server.delete('/environment')
def delete_sensor():
    id = request.form.get('id')

    query = f"""
        DELETE FROM env_data
        WHERE id = {id};
    """

    executeQuery(query=query)

    return "sensor_data deleted successfully"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
