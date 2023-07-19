import pymysql

connect_db = pymysql.connect(host = 'localhost', 
                            port=3306, 
                            user='Adam', 
                            passwd='1019', 
                            charset='utf8', 
                            db='assignment')

