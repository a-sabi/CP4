name = input("Введите имя:")
lastname = input("Введите фамилию:")
birth = int(input("Введите дату рождения:"))
print(name, lastname, birth, sep="_")
name1 = lastname
lastname = name
name = name1
birth += 60
print(name, lastname, birth, sep="_") 