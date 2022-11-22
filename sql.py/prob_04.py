# Задача из презентора от 17.11.22

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_detail(School_id):
 try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = '''SELECT * FROM School WHERE School_Id = ?'''
    cursor.execute(select_query, School_id,)
    records = cursor.fetchall()
    print("Данные по школе")
    for row in records:
        print('ID школы', row[0])
        print("Название школы", row[1])
        print("Колличество мест", row[2])
    close_connection(connection)
 except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

def get_teatcher_detail(teatcher_id):
 try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = '''SELECT * FROM Teatcher WHERE Teatcher_Id = ?'''
    cursor.execute(select_query, (teatcher_id,))
    records = cursor.fetchall()
    print("Данные по учителю")
    for row in records:
        print('ID учителя', row[0])
        print("Имя учителя", row[1])
        print('ID школы', row[2])
        print("Дата начало работы", row[3])
        print("Специализация ", row[4])
        print("Зарплата ", row[5])
        print("Опыт работы ", row[6])
    close_connection(connection)
 except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)
print('Задача 4 данные по учителям из школы')
get_school_detail(1)
print("\n") 
get_teatcher_detail(101)
