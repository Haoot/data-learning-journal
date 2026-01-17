import pymysql                 #导入pymysql库，用来连接MYSQL数据库

conn = pymysql.connect(        #创建一个MySQL数据库对象
    host='localhost',          #本地数据库
    user='root',               #用户名
    password='123456',         #密码
    database='test_db',        #数据库名
)

 # 创建游标
cursor = conn.cursor()

cursor.execute("SELECT VERSION()") #执行SQL，获取当前数据库服务器版本
version = cursor.fetchone()        #获取查询结果中的第一行数据
print(f"MySQL版本 {version[0]}")    #输出结果

# 关闭连接
cursor.close()
conn.close()