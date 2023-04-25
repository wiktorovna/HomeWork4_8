from itertools import count
def my_func(n):
    fact = 1
    for a in count(1):
        if a > n:
            break
        fact = fact * a
        yield fact

n = int(input('Введите целое число n '))
i = 0
for el in my_func(n):
    i +=1
    print(f'Факториал {i} = {el}')

