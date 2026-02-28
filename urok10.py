import sqlite3

conn = sqlite3.connect("c2213.db")
cur = conn.cursor()

'''
cur.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    teacher_surname TEXT
)
""")


cur.execute("INSERT INTO Courses (course_name, teacher_surname) VALUES ('Python', 'Tytarenko')")
cur.execute("INSERT INTO Courses (course_name, teacher_surname) VALUES ('Lego', 'Ugelovskiy')")
cur.execute("INSERT INTO Courses (course_name, teacher_surname) VALUES ('Photoshop', 'Ivanova')")


cur.execute("SELECT name FROM Students")
students = cur.fetchall()


cur.execute("SELECT course_name FROM Courses")
courses = cur.fetchall()

print("Students:", students)
print("Courses:", courses)
'''
'''
cur.execute("SELECT * FROM Students")
data = cur.fetchall()

if data:
    print("Data exist")
else:
    print("Data don`t exist")
'''
name = "Milena"
age = 10 
cur.execute("INSERT INTO Students(name,age) VALUES (?, ?)",(name,age))
cur.execute("SELECT name FROM Students")
students = cur.fetchall()
print("Students", students)



conn.commit()
conn.close()
