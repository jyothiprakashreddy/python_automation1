import pymysql
conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'root')
print('connected')
cur = conn.cursor()
cur.execute('use day1')
cur.execute('select * from schooling')
tables = cur.fetchall()
print(tables)
for x in tables:
    print(x)