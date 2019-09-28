import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Adaptation",
  passwd="team2"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")