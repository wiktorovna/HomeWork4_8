my_file = open('test.txt', 'w', encoding='utf-8')
line = input('Введите текст: ')
while line != '':
    my_file.writelines(line + '\n')
    line = input('Введите текст: ')

my_file.close()
