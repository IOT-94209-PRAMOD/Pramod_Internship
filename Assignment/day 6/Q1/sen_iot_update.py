# import mysql connector
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
id = input("Enter id whose to be updated : ")
humidity = input("Enter new humudity : ")

query = f"update sen_readings SET humidity = '{humidity}' where id = '{id}';"

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
