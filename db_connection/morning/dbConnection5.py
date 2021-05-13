import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'world'
}
cnx = mysql.connector.connect(**config)

my_cursor = cnx.cursor()
query = "SHOW TABLES"

my_cursor.execute(query)

for x in my_cursor:
    print(x)

cnx.close()
