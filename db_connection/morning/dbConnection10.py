# swarnandhra college of engineering and technology

import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root'
}
cnx = mysql.connector.connect(**config)
# print(cnx)

my_cursor = cnx.cursor()

my_cursor.execute("DROP database IF EXISTS scetcse")

query = "CREATE DATABASE scetcse"
my_cursor.execute(query)
