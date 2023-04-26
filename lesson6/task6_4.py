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
        return 'Машина тронулась'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return 'Машина повернула' + direction


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


volkswagen = TownCar('Фольксваген', 60, 'белый')
print(volkswagen.name, volkswagen.color, volkswagen.speed, volkswagen.is_police)
print(volkswagen.go(), volkswagen.turn('налево'), volkswagen.stop())
sport = SportCar('Фольксваген', 90, 'зеленый')
work1 = WorkCar('Фольксваген', 70, 'белый', True)
work2 = WorkCar('бмв', 90, 'красный', False)
police = PoliceCar('Фольксваген', 180, 'красный')
