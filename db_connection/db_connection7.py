# insert data into table


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

query = 'insert into students (name, regno) values(%s, %s)'
val = [("Divya", "123")]

my_cursor.execute(query, val)
mydb.commit()


print(my_cursor.rowcount, 'record inserted')
