def summary():
    try:
        with open('file_5_5.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except ValueError:
        print('Ошибка ввода данных')
summary()
