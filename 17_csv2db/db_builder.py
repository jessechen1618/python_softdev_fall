#Jesse "McCree" Chen
#SoftDev  
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#Part 1
command = "CREATE TABLE IF NOT EXISTS classData (courses TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

csvfile = open('courses.csv', newline = '')
reader = csv.DictReader(csvfile)
for row in reader:
	command = "INSERT INTO classData VALUES(\"" + row['code'] + "\"," + row['mark'] + "," + row['id'] + ")"
	c.execute(command)


# Part 2
command = "CREATE TABLE IF NOT EXISTS studentData (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

csvfile = open('students.csv', newline='')
reader = csv.DictReader(csvfile)
for row in reader:
	print(row)
	command = "INSERT INTO studentData VALUES(\"" + row['name'] + "\"," + row['age'] + "," + row['id'] + ")"
	c.execute(command)
#==========================================================

db.commit() #save changes
db.close()  #close database


