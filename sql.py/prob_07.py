# Задача 7 от 17.11.2022

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = '''SELECT * FROM School WHERE School_id = ?'''
    cursor.execute(select_query, (school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1] #наименование школы
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

def get_teatcher(school_id):
   try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    select_query = '''SELECT * FROM Teatcher WHERE School_id = ?'''
    cursor.execute(select_query, (school_id,))
    records =cursor.fetchall()

    print("Учителя из школы", school_name)    
    for row in records:
        print('ID учителя', row[0])
        print("Имя учителя", row[1])
        print('ID школы', row[2])
        print("Название школы", school_name)
        print("Дата начало работы", row[3])
        print("Специализация ", row[4])
        print("Зарплата ", row[5])
        print("Опыт работы ", row[6], "\n")
    close_connection(connection)
   except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

print ("Задача №6 \n")
get_teatcher(3)