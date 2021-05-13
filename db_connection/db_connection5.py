# creating a table

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'sietcse'
}

mydb = mysql.connector.connect(**config)


# cursor
my_cursor = mydb.cursor()
query = 'create table students(name varchar(255), regno varchar(255))'


my_cursor.execute(query)
