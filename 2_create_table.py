import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="poem_database_big_data"
)


mycursor = mydb.cursor()

drop_table_if_exist = "DROP TABLE IF EXISTS poem_table"

query = """CREATE TABLE poem_table (  
         id INT AUTO_INCREMENT primary key NOT NULL,
         poem TEXT NOT NULL,  
         topic VARCHAR(64) NOT NULL 
         ) """
  

mycursor.execute(drop_table_if_exist)
mycursor.execute(query)

print("Poem table is created in the database")

mydb.commit()
mycursor.close()
mydb.close()
