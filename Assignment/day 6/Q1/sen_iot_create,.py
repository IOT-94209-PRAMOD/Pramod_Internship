# import mysql connector
from datetime import datetime as dt
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_sen",
    use_pure = True
)

# form a query to be executed
id = int(input("Enter id : "))
temperature = input("Enter temp : ")
humidity = input("Enter humidity : ")
#timesamp = input(f"Enter timesamp: {(dt.new())}")

query = f"insert into sen_readings values({id}, '{temperature}', '{humidity}', '{dt.now()}');"

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
