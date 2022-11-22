# Задача № 5 17.11.2022

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_teatchers_list(speciality, salary):
 try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = '''SELECT * FROM Teatcher WHERE Speciality = ? AND Salary > ?'''
    cursor.execute(select_query, (speciality, salary))
    records = cursor.fetchall()
    print("Учитель со специальностью", speciality, "и зарплатой больше", salary)
    for row in records:
        print('ID учителя', row[0])
        print("Имя учителя", row[1])
        print('ID школы', row[2])
        print("Дата начало работы", row[3])
        print("Специализация ", row[4])
        print("Зарплата ", row[5])
        print("Опыт работы ", row[6], "\n")
    close_connection(connection)
 except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)
print("Задача 5 Список учителей \n")
get_teatchers_list("Информатик" , 30000)

