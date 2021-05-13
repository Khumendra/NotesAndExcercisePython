import mysql.connector
from mysql.connector import cursor

config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database":'world'
}


mydb = mysql.connector.connect(**config)
# print(mydb)

# cursor
my_cursor = mydb.cursor()
# print(my_cursor)
query = 'show tables'

my_cursor.execute(query)
print(*my_cursor, sep='\n')
