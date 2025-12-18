# import mysql connector
import mysql.connector
from datetime import datetime as dt
# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database ="smart_agri_iot",
    use_pure = True
)

# form a query to be executed
sensor_id = int(input("Enter sensor_id : "))
moisture_level = input("Enter moisture_level : ")
# date_and_time= input( )


query = f"insert into smart_agri_iot values({sensor_id}, '{moisture_level}', '{dt.now()}');"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()