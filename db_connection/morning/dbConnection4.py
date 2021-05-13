# show databases

import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root'
}
cnx = mysql.connector.connect(**config)

my_cursor = cnx.cursor()
query = "SHOW DATABASES"
my_cursor.execute(query)

print(*my_cursor, sep='\n')

cnx.close()
