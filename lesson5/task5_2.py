my_file = open('file_5_2.txt', 'r')

content = my_file.readlines()
print(f'Количество строк в файле: {len(content)}')

i = 1
for line in content:
    print(f'Общее количество слов {i} - ой строки:{len(line.split())}')
    i += 1

my_file.close()
