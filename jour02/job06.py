import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = '****',
    password = '*********',
    database = '*********',
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute('SELECT SUM(capacite) FROM salle')
cursor = mycursor.fetchone()[0]
print(f"La capacité de toutes les salles est : {cursor} ")

mycursor.close()
mydb.close()
