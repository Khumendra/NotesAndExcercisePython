# show the db
# select or use any db
# table
import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database":'world'
    
}
cnx = mysql.connector.connect(**config)

my_cursor = cnx.cursor()

query = "select * from city"

my_cursor.execute(query)
# print(*my_cursor, sep='\n')
with open("mycity.txt",'w') as mycity:
    for i in my_cursor:
        # mycity.writelines(str(i))
        mycity.writelines("")
