
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO Teatcher (Teatcher_Id, Teatcher_Name, School_Id,
Joining_Date, Speciality, Salary, Experience)
VALUES
('101', 'Галина', '1', '2021-2-10', 'Физик', '40000', NULL),
('102', 'Мария', '1', '2018-07-23', 'Химик', '20000', NULL),
('103', 'Ольга', '2', '2022-05-19', 'Информатик', '25000', NULL),
('104', 'Полина', '2', '2017-12-28', 'Физик ', '28000', NULL),
('105', 'Лидия', '3', '2015-06-04', 'Информатик', '42000', NULL),
('106', 'Анастасия', '3', '2019-09-11', 'Учитель трудов', '30000', NULL),
('107', 'Ирина', '4', '2020-08-21', 'Информатик', '32000', NULL),
('108', 'Виктория', '4', '2017-10-17', 'Географ', '30000', NULL);
"""
cursor.execute(query)
connection.commit()
connection.close()

