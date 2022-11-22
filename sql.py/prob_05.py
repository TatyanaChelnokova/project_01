# Создание таблицы скул

import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO School (School_Id, School_Name, Place_Count)
VALUES
('1', 'Протон', 200),
('2', 'Преспектива', 300),
('3', 'Спектр', 400),
('4', 'Содружество', 500);
);
"""
cursor.execute(query)
connection.commit()
connection.close()
