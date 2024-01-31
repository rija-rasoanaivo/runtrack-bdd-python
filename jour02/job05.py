import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = '****',
    password = '*********',
    database = '*********',
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute('SELECT SUM(superficie) FROM etage')
cursor = mycursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {cursor} m2")

mycursor.close()
mydb.close()
