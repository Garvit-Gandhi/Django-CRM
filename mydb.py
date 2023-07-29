import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='garvit2002',

    )

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE dbname")
print("Done!")