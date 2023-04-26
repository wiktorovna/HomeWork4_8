import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_5_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль - {prof_aver:.2f}')
    else:
        print(f'Прибыль =0')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_5_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(profit, write_js, ensure_ascii=False)

    js_str = json.dumps(profit)
    print(f'json объект: \n '
          f'Средняя прибыль {js_str}')
