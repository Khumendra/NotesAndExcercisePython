import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user="root",
    password="root",
    database='scetcse'
)

my_cursor = cnx.cursor()

query = "INSERT INTO students(name, regno) values (%s, %s)"
val = ("Vikash", "ST01")

my_cursor.execute(query, val)


cnx.commit()
