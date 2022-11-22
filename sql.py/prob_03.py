# Подключении к версии БД

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def read_db():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = ("SELECT sqlite_version();")
    cursor.execute(query)
    version = cursor.fetchone()
    print ("Вы подключились к версии ", version)
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных ", error)

print ("Задача №2 Версия БД")
read_db()