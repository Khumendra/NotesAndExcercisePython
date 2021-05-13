import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'sietcse'
}

mydb = mysql.connector.connect(**config)

my_cursor = mydb.cursor()

query = "select * from students"
my_cursor.execute(query)

# getting all the records
student = my_cursor.fetchall()

print(student)
# for i in student:
# 	print(i)

