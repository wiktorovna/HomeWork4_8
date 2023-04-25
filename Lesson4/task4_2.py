my_list = [4, 3, 2, 5, 14, 6, 3, 9, 12, 45]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list)
