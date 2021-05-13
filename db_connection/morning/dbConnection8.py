import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'world'
}

cnx = mysql.connector.connect(**config)

my_cursor = cnx.cursor()
query = "SELECT * FROM CITY"

my_cursor.execute(query)

with open('city.csv', 'w') as file:
    for line in my_cursor:
        # file.writelines(str(line))
        file.writelines('')

