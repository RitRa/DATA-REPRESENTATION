import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='Password!',
                             db='datarepresentation',
                             #charset='utf8mb4',
                             
                             #cursorclass=pymysql.cursors.DictCursor
                             )

cursor = conn.cursor()  


sql= "DELETE from student where id=%s"
values=(1, )

cursor.execute(sql, values) 

conn.commit()

print ("delete!!")


