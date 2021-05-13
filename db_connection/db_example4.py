import mysql.connector

cnx = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="root"
)

my_cursor = cnx.cursor()
query = "SHOW DATABASES"
my_cursor.execute(query)

print(*my_cursor, sep="\n")