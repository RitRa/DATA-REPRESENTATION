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


sql= "Insert into student (firstname, age) values (%s, %s)"
values=("Mary", 21)
cursor.execute(sql, values) 

conn.commit()

print("1 record inserted,   ID", cursor.lastrowid)
