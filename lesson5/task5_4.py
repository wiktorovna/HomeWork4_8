rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

new_file = []
with open('file_5_4.txt', 'r') as file_obj:
    for line in file_obj:
        words = line.split(' - ')
        new_file.append(rus[words[0]] + ' - ' + words[1])
    print(new_file)

with open('file_5_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
