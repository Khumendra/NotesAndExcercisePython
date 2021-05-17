import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user="root",
    password="root",
    database='world'
)

my_cursor = cnx.cursor()
my_cursor.execute('select * from countrylanguage')
data = my_cursor.fetchall()
print(my_cursor.rowcount)
print(*data, sep='\n')