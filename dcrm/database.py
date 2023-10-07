import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd='hoshi'
    
)
#prepare a cursur object 
cursorObject= database.cursor()

#create  the database
cursorObject.execute("CREATE DATABASE mydb")

print("Done!!")
