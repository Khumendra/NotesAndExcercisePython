import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user="root",
    password="root",
    database='scetcse'
)

my_cursor = cnx.cursor()
query = "INSERT INTO students(name, regno) VALUES (%s, %s)"
val = [
    ('STU3', 'ST03'),
    ('STU4', 'ST04'),
    ('STU5', 'ST05'),
    ('STU6', 'ST06'),
    ('STU7', 'ST07'),
    ('STU8', 'ST08'),
]

my_cursor.executemany(query, val)
print(my_cursor.rowcount, 'successfully added')

cnx.commit()