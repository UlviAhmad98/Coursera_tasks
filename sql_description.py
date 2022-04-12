###SQLite module
import sqlite3
###Connection establishment (create a temporary database in RAM)
con = sqlite3.connect('example.db')
###Curson object 
cur = con.cursor()
###'execute()' for SQL commands
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')
###Inserting data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
###Iterator
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
###Save changes
con.commit()
###Close the connection
con.close()
