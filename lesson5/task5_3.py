name_salery = {'Ivanov': 29000, 'Petrov': 50000, 'Sidorov': 19000, 'Belui': 35000, 'Kukushkin': 58900,
               'Chernui': 15000, 'Smart': 100000, 'Clever': 90000, 'Politely': 21000, 'Interesting': 13000}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in name_salery.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print('Неверно введены данные')
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f'Средний доход работников = {result}')
