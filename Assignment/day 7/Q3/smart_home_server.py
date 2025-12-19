# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/smart_home', methods=['POST'])
def create_student():
    # extract data form form
    id = request.get_json().get('id')
    light = request.get_json().get('light')
    fan = request.get_json().get('fan')
    temperature = request.get_json().get('temperature')

    # create a query to add student into table
    query = f"insert into smart_home values({id}, '{light}', '{fan}', '{temperature}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "home_data is added successfully"

@server.route('/smart_home', methods=['GET'])
def retrieve_students():
    # create a select query
    query = "select * from smart_home;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"smart_home : {data}"

@server.route('/smart_home', methods=['PUT'])
def update_student():
    # extract data form form
    id = request.get_json().get('id')
    fan = request.get_json().get('fan')

    # create a query
    query = f"update smart_home SET fan = '{fan}' where id = '{id}';"

    # execute the query
    executeQuery(query=query)

    return "email is updated successfully"

@server.route('/smart_home', methods=['DELETE'])
def delete_student():
    # extract data form form
    light = request.get_json().get('light')

    # create a query
    query = f"delete from smart_home where light = '{light}';"

    # execute the query
    executeQuery(query=query)

    return "home data is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)