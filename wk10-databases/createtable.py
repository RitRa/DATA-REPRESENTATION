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


sql = ('create table student (id int NOT NULL auto_increment,firstname varchar(100),age int(3),PRIMARY KEY(id));') 
cursor.execute(sql) 
print ("table added!!")


