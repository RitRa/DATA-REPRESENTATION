import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='Password!',
                             #db='datarepresentation',
                             #charset='utf8mb4',
                             
                             #cursorclass=pymysql.cursors.DictCursor
                             )
print ("connect successful!!")

print(conn)


cursor = conn.cursor()  


sql = ('create database datarepresentation;') 
cursor.execute(sql) 
print ("Database created!!")

