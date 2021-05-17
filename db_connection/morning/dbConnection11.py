import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'scetcse'
}
cnx = mysql.connector.connect(**config)
# print(cnx)

my_cursor = cnx.cursor()
query = 'CREATE TABLE students (name VARCHAR(255), regno VARCHAR(4))'

my_cursor.execute(query)

