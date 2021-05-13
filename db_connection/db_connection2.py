
import mysql.connector

config = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "database": "world"
}

cnx = mysql.connector.connect(**config)


my_cursor = cnx.cursor()
# print(my_cursor)
query = "select * from city"
my_cursor.execute(query)



# print(*my_cursor, sep=' \n')
with open('city.txt','w') as file:
    for line in my_cursor:
        file.writelines(str(line))
