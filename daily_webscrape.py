import mysql.connector
import scrape_functions

cities = ['los angeles, ca', 'new york, ny', 'boston, ma']
searches = ['data scientist','data engineer']

df = scrape_functions.scrape_many_jobs(cities,searches)


mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Kiwi1812!",
      database="test")

        
vals = df.to_records(index=False)
vals = vals.tolist()
    
mycursor = mydb.cursor()

sql = "INSERT INTO joblist (title, company, date, location, search) VALUES (%s, %s, %s, %s, %s)"

mycursor.executemany(sql, vals) #vals should be a list of tuples ('job 1','title 1','date 1'), ('job 2','title 2','date 2'),

mydb.commit()

print(mycursor.rowcount, "was inserted.") #checks if it works