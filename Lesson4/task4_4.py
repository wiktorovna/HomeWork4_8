my_list = [2, 5, 11, 15, 4, 1, 1, 5, 10, 11, 3, 4, 19]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
