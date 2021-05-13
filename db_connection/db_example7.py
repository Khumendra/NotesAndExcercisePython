# create DB

import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
}
cnx = mysql.connector.connect(**config)

my_cursor = cnx.cursor()
query = "CREATE DATABASE mydb1"
my_cursor.execute(query)
