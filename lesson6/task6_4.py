# -*- coding: cp1251 -*-
class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return '������ ���������'

    def stop(self):
        return '������ ������������'

    def turn(self, direction):
        return '������ ���������' + direction


class TownCar(Cars):
    family = None

    def __init__(self, name, speed, color, family=True):
        super().__init__(name, speed, color)
        self.family = family


class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


volkswagen = TownCar('�����������', 60, '�����')
print(volkswagen.name, volkswagen.color, volkswagen.speed, volkswagen.is_police)
print(volkswagen.go(), volkswagen.turn('������'), volkswagen.stop())
sport = SportCar('�����������', 90, '�������')
work1 = WorkCar('�����������', 70, '�����', True)
work2 = WorkCar('���', 90, '�������', False)
police = PoliceCar('�����������', 180, '�������')
