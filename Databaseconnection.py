import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="Tarun",passwd="groot@1",database="tokas")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchone()

for i in result:
    print(i)

