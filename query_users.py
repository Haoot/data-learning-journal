import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='test_db',
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

for row in results:
    print(f"ID:{row[0]}, Name:{row[1]}")

cursor.close()
conn.close()