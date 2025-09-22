import pymysql



conn = pymysql.connect(
                        host='sql7.freesqldatabase.com',
                        database='sql7799676',
                        user = 'sql7799676',
                        password='JLlBmAbByt',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
)

cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS book")
sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY AUTO_INCREMENT ,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL 
)"""
cursor.execute(sql_query)
conn.close()