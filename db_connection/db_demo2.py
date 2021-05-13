from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='root',
                                 host='127.0.0.1',
           )

print("MySQLConnection", cnx)                      
cnx.close()

