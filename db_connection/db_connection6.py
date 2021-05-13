# show tables;

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database':'sietcse'
}

mydb = mysql.connector.connect(**config)


# cursor
my_cursor = mydb.cursor()
# query = 'show tables'
query = 'select * from students'

my_cursor.execute(query)
print(*my_cursor)
