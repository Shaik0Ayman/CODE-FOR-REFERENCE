a = "0786"
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=a,

)

cursor = mydb.cursor()
cursor.execute('show databases')
for i in  cursor:
   print(i)




'''cursor = mydb.cursor()
cursor.execute('show tables')
for i in  cursor:
   print(i)'''
     

'''cursor = mydb.cursor()
cursor.execute('show databases')
for i in cursor:
    print(i)'''

