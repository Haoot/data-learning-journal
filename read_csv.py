file = open('data/users.csv', 'r', encoding='utf-8')
for line in file:
    print(line.strip())
file.close()
