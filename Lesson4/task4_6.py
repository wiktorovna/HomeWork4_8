from itertools import count
from itertools import cycle
def my_count_func(number_start, number_stop):
    for el in count(number_start):
        if el > number_stop:
            break
        else:
            print(el)
def my_cycle_func(my_list, iteration):
    i = 0
    q = cycle(my_list)
    while i < iteration:
        print(next(q))
        i+=1
my_count_func(number_start = int(input('Введите первое число ')), number_stop = int(input('Введите последнее число ')))
my_cycle_func(my_list = [3, 2, 18], iteration = int(input('Введите количество повторений: ')))

