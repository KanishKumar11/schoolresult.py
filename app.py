import mysql
from sqlite3 import Cursor
import mysql.connector
from mysql.connector import Error


def con(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("success")
    except Error as err:
        print("Error")
    return connection

pw = "kanish@7.7"
db = "result"

connection = con("localhost","root",pw)

#db connection
def condb(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name)
        print("db connectd")
    except Error as err:
        print("error2")
    return connection


#sql commands

def query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("qsucces")
    except Error as err:
        print("error3")

roll = str(input("Enter roll no\n"))
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print("error4 '{err}'")

#Getting Data
q1 = 'select * from result where Roll =' +roll+';'
connection = condb("localhost","root",pw,db)
results = read_query(connection, q1)
for result in results:
    print("Name: "+result[2])
    print("Gender: "+result[1])
    print("Roll no: "+str(result[0]))
    print("SUB CODE: "+str(result[3])+" Marks: "+ str(result[4])+" GRADE: "+result[5])
    print("SUB CODE: "+str(result[6])+" Marks: "+ str(result[7])+" GRADE: "+result[8])
    print("SUB CODE: "+str(result[9])+" Marks: "+ str(result[10])+" GRADE: "+result[11])
    print("SUB CODE: "+str(result[12])+" Marks: "+ str(result[13])+" GRADE: "+result[14])
    print("SUB CODE: "+str(result[15])+" Marks: "+ str(result[16])+" GRADE: "+result[17])
    print("SUB CODE: "+str(result[18])+" Marks: "+ str(result[19])+" GRADE: "+result[20])
    print("Result: " + result[21])

input()