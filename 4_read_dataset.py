import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="poem_database_big_data"
)


mycursor = mydb.cursor()

query = "SELECT * FROM poem_table"
  

mycursor.execute(query)

results = mycursor.fetchall()

for row in results:
  print(row)


mydb.commit()
mycursor.close()
mydb.close()