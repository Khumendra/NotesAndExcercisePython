import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='world')

if cnx:
    print("Connected.")                              
cnx.close()