from mysql.connector import (connection)

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root'
}

cnx = connection.MySQLConnection(**config)

print(cnx)
if cnx:
    print("Connected")
