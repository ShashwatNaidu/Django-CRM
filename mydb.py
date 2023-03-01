import mysql.connector

database = mysql.connector.connect( host = 'localhost', user = 'CR7', passwd = 'Ronaldo@07')

#prepare a cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("Done setting up database in mysql")