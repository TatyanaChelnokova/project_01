# Общение с БД 4 щаг

import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = "SELECT * FROM School;"
cursor.execute(query)
record = cursor.fetchall()
connection.close()
print(record)

