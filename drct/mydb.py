# creating new database

import mysql.connector

# setting conncetion to database
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Viv@9411',

)

# perpare a cursor object
cursorObject = dataBase.cursor()

# create a databse
cursorObject.execute("CREATE DATABASE college")

print ("ALL done")