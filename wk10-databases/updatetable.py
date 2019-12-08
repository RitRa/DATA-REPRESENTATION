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


sql= "UPDATE student set firstname=%s, age=%s where id=%s"
values=("Joe", 33, 1)

cursor.execute(sql, values) 

result = cursor.fetchall()

for x in result:
    print(x)

conn.commit()