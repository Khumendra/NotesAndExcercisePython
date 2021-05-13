import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database':'sietcse'
}

mydb = mysql.connector.connect(**config)

my_cursor = mydb.cursor()
query = 'insert into students (name, regno) values(%s, %s)'

val = [
    ("Vidya", "324"),
    ("Ajay", "124"),
    ("Uma", "423"),
    ("Vijay", "223"),
]


my_cursor.executemany(query, val)

mydb.commit()

print(my_cursor.rowcount, 'record inserted')
