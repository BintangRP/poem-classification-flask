import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="poem_database_big_data"
)


mycursor = mydb.cursor()

query = """INSERT INTO poem_table (poem ,topic) 
          VALUES (%s, %s)"""
  

# Load data into the database
data = pd.read_csv('data.csv\data.csv')

# print("dataset load --> ",data)

for index, row in data.iterrows():
    # print(row[2])
#     print(index)
  # print(row[1])
    # print(row['topic'])
    mycursor.execute(query, (row[1], row[2]))


mydb.commit()
mycursor.close()
mydb.close()