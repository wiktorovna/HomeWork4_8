from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(pr_el, el):
    return pr_el * el

print(f'Произведение всех четных чисел массива: {reduce(my_func, my_list)}')

