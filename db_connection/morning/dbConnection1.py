# import
import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

# connection
print(cnx)
if cnx:
    print("Connected Successfully!")

cnx.close()
