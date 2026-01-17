import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test_db",
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

output_file = open('output/users_form_mysql.csv', 'w', encoding='utf-8')
output_file.write('id,Name\n')

for row in results:
    line =f"{row[0]},{row[1]}\n"
    output_file.write(line)

output_file.close()
print("数据已导出到 output/users_form_mysql.csv")

cursor.close()
conn.close()