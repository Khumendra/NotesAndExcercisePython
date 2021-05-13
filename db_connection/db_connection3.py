# create db
import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost'
}


cnx = mysql.connector.connect(**config)


# cusor
my_cursor = cnx.cursor()
my_cursor.execute("CREATE DATABASE sietcse")

# Swarnandhra Institute of Engineering and Technology
