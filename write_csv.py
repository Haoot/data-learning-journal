import random  # 随机数模块

# 准备数据
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
cities = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou', 'Hangzhou']

# 第1步：打开文件（写入模式）
file = open('data/random_users.csv', 'w', encoding='utf-8')

# 第2步：写表头
file.write('id,name,age,city\n')

# 第3步：循环100次生成数据
for i in range(1, 101):  # i从1到100
    name = random.choice(names)  # 随机选一个名字
    age = random.randint(20, 40)  # 随机生成20-40之间的年龄
    city = random.choice(cities)  # 随机选一个城市

    # 拼接成一行，写入文件
    line = f"{i},{name},{age},{city}\n"
    file.write(line)

# 第4步：关闭文件
file.close()

print("100条随机用户数据已生成到 data/random_users.csv")