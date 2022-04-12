import sqlite3

con=sqlite3.connect('family.sqlite')
cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS Family')
cur.execute('CREATE TABLE Family (name TEXT, age INTEGER, gender TEXT) ')

while True:
    namex=input('Enter the name: ')
    agex=input('Enter the age: ')
    genderx=input('Enter the gender: ')
    if namex=='ESC':
        break
    else:
        cur.execute('INSERT INTO Family (name, age, gender) VALUES(?,?,?)', (namex, agex, genderx))
        
con.commit()

cur.execute('SELECT * FROM Family ORDER BY age')
print(cur.fetchall())
con.commit()

cur.close()