import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE poem_database_big_data")

print("Database poem created")

mydb.commit()

mycursor.close()

mydb.close()