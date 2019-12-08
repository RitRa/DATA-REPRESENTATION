import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='Password!',
                             db='datarepresentation',
                             #charset='utf8mb4',
                             
                             #cursorclass=pymysql.cursors.DictCursor
                             )
print ("connect successful!!")

print(conn)


cursor = conn.cursor()  


sql= "Select * from student"
#values=(1,)

cursor.execute(sql) 
result = cursor.fetchall()

for x in result:
    print(x)


