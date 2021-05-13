import mysql.connector

cnx = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="root"
)

print(cnx)
if cnx:
    print("Successfully Connected")
