# Опыт работы всех учителей 

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def insert_experience():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    update_query = ("UPDATE Teatcher SET Experience = 5 WHERE Experience is NULL")
    cursor.execute(update_query)
    connection.commit()
    connection.close()

  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных ", error)

print('Задача 3 Апдейт опыт работы')
insert_experience()
print("Опыт работы обновлен")

