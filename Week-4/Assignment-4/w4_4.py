import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1019",
    database = "assignment"
    )

my_cursor = mydb.cursor()

my_cursor.execute("CREATE TABLE article (\
                  id INTEGER AUTO_INCREMENT PRIMARY KEY,\
                  user_id INTEGER,\
                  FOREIGN KEY (user_id) REFERENCES user(id),\
                  article VARCHAR(100),\
                  content VARCHAR(100))")

for i in range(1,31):
    sql = "INSERT INTO article (user_id, article, content) VALUES (%s, %s, %s)"
    record = (1,f"a{i}",f"c{i}")
    my_cursor.execute(sql, record)

mydb.commit()
my_cursor.close()
mydb.close()