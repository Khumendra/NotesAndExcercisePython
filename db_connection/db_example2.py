from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='root',
                                 host='localhost',
                                )
cnx.close()