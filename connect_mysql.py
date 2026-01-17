import pymysql

conn = pymysql.connect(
    host='localhost',          #本地数据库
    user='root',               #用户名
    password='123456',         #密码
    database='test_db',        #数据库名
)

 # 创建游标
cursor = conn.cursor()

#执行SQL
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(f"MySQL版本 {version[0]}")

# 关闭连接
cursor.close()
conn.close()