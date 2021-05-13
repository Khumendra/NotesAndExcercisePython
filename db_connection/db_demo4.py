import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="world"

)

# mydb.cursor.execute("Show Databases")
cursor = mydb.cursor()
cursor.execute("select * from city")
# x = cursor.fetchall()
# print(x) 
with open("city.txt", "w") as city:
    for city_detail in cursor:
        # city.writelines(str(city_detail))
        city.writelines(str(""))
        
