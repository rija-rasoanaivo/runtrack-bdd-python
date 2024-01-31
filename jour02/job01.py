import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = '***',
    password = '*********',
    database = '*********',
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute('SELECT * FROM etudiant')
print(mycursor.fetchall())

mycursor.close()
mydb.close()
