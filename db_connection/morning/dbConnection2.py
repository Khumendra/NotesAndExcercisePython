# import
from mysql.connector import (connection)

# connection
cnx = connection.MySQLConnection(
    host='localhost',
    user='root',
    password='root'
)

print(cnx)
if cnx:
    print("Successfully Connected")

cnx.close()
