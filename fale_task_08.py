# Самостоятельная работа 17.11.2022

# import sqlite3

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students 
# (
# Students_Id INTEGER NOT NULL, 
# Students_Name TEXT NOT NULL, 
# School_Id INTEGER NOT NULL PRIMARY KEY
# );
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

# import sqlite3

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Students_Id, Students_Name, School_Id) 
# VALUES 
# ('201', 'Иван', 1), 
# ('202', 'Петр', 2), 
# ('203', 'Анастасия', 3), 
# ('204', 'Игорь', 4);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()


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
    return record[1] 
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

def get_students(school_id):
   try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    select_query = '''SELECT * FROM Students WHERE School_id = ?'''
    cursor.execute(select_query, (school_id,))
    records =cursor.fetchall()
 
    for row in records:
        print('ID студента', row[0])
        print("Имя студента", row[1])
        print('ID школы', row[2])
        print("Название школы", school_name)
    close_connection(connection)
   except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

print ("Самостоятельная работа \n")
get_students(3)

