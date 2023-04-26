import re

courses = {}
with open('file_5_6.txt', 'r') as init_f:
    for line in init_f:
        words = line.split()
        course = words[0]
        sum = 0
        for word in words[1:]:
            result = re.sub(r'[^0-9]', '', word)
            if(result == ''):
                result = '0'
            sum = sum + int(result)
        courses[course] = result

print(f'Общее количество часов по предметам - {courses}')
