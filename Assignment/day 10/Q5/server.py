# from flask import Flask, request
# from datetime import datetime as dt
# from executequery import executeQuery

# server = Flask(__name__)

# @server.route('/', methods=['GET'])
# def homepage():
#     return "This is a homepage"

# @server.route('/humidity', methods=['POST'])
# def create_temperature():
#     flag=1
#     if(flag):
#         query = f"""
# INSERT INTO smart_agri_iot (sensor_id, moisture_level, date_and_time)
# VALUES (1,0, '{dt.now()}');
# """

#         executeQuery(query=query)
#         flag=0

#     humidity = request.get_json().get('humidity')
#     query=f"update smart_agri_iot SET moisture_level={humidity} where sensor_id=1;"
#     executeQuery(query=query)
#     print(f"humidity = {humidity}")

#     return "humidity is received"

# if __name__ == '__main__':
#     server.run(host='0.0.0.0', port=4000, debug=True)


from flask import Flask, request, jsonify
from datetime import datetime
from executequery import executeQuery

server = Flask(__name__)

@server.route('/', methods=['GET'])
def homepage():
    return "This is a homepage"

@server.route('/humidity', methods=['POST'])
def receive_humidity():
    data = request.get_json()

    if not data or 'humidity' not in data:
        return jsonify({"error": "Humidity value missing"}) 

    humidity = data['humidity']
    sensor_id = 1
    current_time = datetime.now()

    query = f"""
    INSERT INTO smart_agri_iot (sensor_id, moisture_level, date_and_time)
    VALUES ({sensor_id}, {humidity}, '{current_time}')
    """

    executeQuery(query=query)

    print(f"Humidity received: {humidity}")

    return jsonify({"message": "Humidity stored successfully"})

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
