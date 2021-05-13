# db connection

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': "sietcse"
}

mydb = mysql.connector.connect(**config)

if mydb:
    print("Connection succesful")
