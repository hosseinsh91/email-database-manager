import re
import mysql.connector
cnx = mysql.connector.connect(user='',password='',
                              host='',
                              database='')

mycursor = cnx.cursor()
email=str(input('Enter Your TABLE name: '))
mycursor.execute("CREATE TABLE %s (username VARCHAR(300), password VARCHAR(300))" % email)
username=str(input('Enter your Email: '))
while re.search(r'^\w+([A-z0-9]?\w+)*@\w+([A-z0-9]?\w+)*\.\w[A-z]+$', username)==None :
    print('Please enter a valid email.\nexample : expression@string.string')
    username=str(input('Enter your Email: '))
password=str(input('Enter your Password: '))
while re.search(r'^\w[A-z0-9]{5,}$',password)==None:
    print('Wrong Password')
    password=str(input('Enter your Password: '))
cursor= cnx.cursor()
cursor.execute(' INSERT INTO %s VALUES  (\'%s\' , \'%s\' )' % (email, username , password ))
cnx.commit()
cnx.close()


