from sys import argv

file_name, first_name, worked_hour, salary, bonus = argv
def calculation_salary (worked_hour, salary, bonus):
    try:
        calculation = (int(worked_hour) * int(salary)) + int(bonus)
        print(f'Ваш доход с учетом бонуса составит {calculation} рублей')
    except TypeError:
        print('Неподходящий тип данных')
        exit()
calculation_salary (worked_hour, salary, bonus)

