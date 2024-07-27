import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1984qaWS',

	)

# настройка cursor object
cursorObject = dataBase.cursor()

# создание БД
cursorObject.execute("CREATE DATABASE d_crm")

print("All done!")
