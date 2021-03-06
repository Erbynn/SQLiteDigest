# This is a hands-on sql database done to understand databases
# Date: 17th November, 2018
# Author: John K. Erbynn 

import sqlite3

#CONNECTING TO DB
# conn = sqlite3.connect("student.db")  # causes error when testing db
conn = sqlite3.connect(":memory:")  # this db will be stored in memmory ... does not cause any error when run several times cus of its refresh rate...very useful for testing
print("Database opened successfully", end='\n\n')


#CREATING TABLE
curs = conn.cursor()

curs.execute(""" CREATE TABLE student(
                    id INT PRIMARY KEY NOT NULL,
                    firstName TEXT NOT NULL,
                    lastName TEXT NOT NULL,
                    age INT NOT NULL);
                    """)
print("Table created successfully")






# INSERT OPERATION
# curs.execute(""" INSERT INTO student VALUES(1, 'john', "kwesi", 22)""")
# curs.execute(""" INSERT INTO student VALUES(2, 'max', "nio", 20)""")
# curs.execute(""" INSERT INTO student VALUES(3, 'joe', "xoa", 22)""")
# i = 4
# fn = "mathew"
# ln = "omeh"
# old = 24
# curs.execute(""" INSERT INTO student VALUES(?, ?, ?, ?)""", (i, fn, ln, old)) #not appropriate for one tuple ... needs to be (i,)...not forgetting the ','
# i2 = 5
# fn2 = "matheee"
# ln2 = "omehee"
# old2 = 24
# curs.execute(" INSERT INTO student VALUES(:id, :firstName, :lastName, :age)", {"id": i2, "firstName": fn2, "lastName": ln2, "age": old2}) #dict format is better
# conn.commit()
# print("Records created into table succesfuly")



#MAKING QUERIES
# curs.execute(" SELECT * FROM student WHERE age = ?", (20,))
# curs.execute(" SELECT * FROM student WHERE age > :age", {'age': 22})
# curs.execute(" SELECT * FROM student")
# getData = curs.fetchall()
# # print(getData)
# # print(getData)

    
# conn.close()












##############into functions########################
def createTable():
    curs.execute(""" CREATE TABLE student(
                        id INT PRIMARY KEY NOT NULL,
                        firstName TEXT NOT NULL,
                        lastName TEXT NOT NULL,
                        age INT NOT NULL);
                        """)
    print("Table created successfully")


def insertStu(ide, fn, ln, yr):
    with conn:  #takes care of the commit on insert,delete,update operation 
        curs.execute(" INSERT INTO student VALUES(:id, :firstName, :lastName, :age) ",  {"id": ide, "firstName": fn, "lastName": ln, "age": yr}) #dict format is better
        # curs.execute(" INSERT INTO student VALUES(?, ?, ?, ?) ", (ide, fn, ln, yr)) #dict format is better
        print("Record created into table succesfully")

def getAllStu():
    curs.execute(" SELECT * FROM student")
    for row in curs.fetchall():
        print(row)

def getStuByAge(age):
    curs.execute(" SELECT * FROM student WHERE age = :age", {'age': age})
    print("done")
    return curs.fetchall()
# getStuByAge(22)

def getData():
    curs.execute(" SELECT * FROM student")
    for row in curs.fetchall():
        print( "ID: ", row[1])
        print( "FirstName: ", row[2])
        print( "LastName: ", row[3])
        print( "Age: ", row[3])


fn = "papa"
ln = "erb"
insertStu(7, fn, ln, 23)
fn = "papa"
ln = "erb"
insertStu(8, fn, ln, 23)

print(getAllStu())

getData()