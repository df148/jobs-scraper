import mysql.connector


#creating jobs database
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Kiwi1812!")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE jobs_database")

#creating jobs table
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="######", #your password goes here
      database="jobs_database")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE jobs(title VARCHAR(255), company VARCHAR(255), location VARCHAR(255), date VARCHAR(255), search VARCHAR(255))")
