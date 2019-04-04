import pymysql
from public import Config

conn=pymysql.connect(**Config.sql_connect_dict)
cur=conn.cursor()
sql="SELECT * from phome_enewsadminstyle"
cur.execute(sql)
cur.fetchone()
print(cur.execute(sql))
print(cur.fetchone())

cur.close()
conn.close()