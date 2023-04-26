class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Создать новый объект дорога')

    def intake(self):
        self.weigth = 40
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Вам нужно {intake} тон асфальта для строительства этой дороги')


road_to_village = Road(50000, 9)
road_to_village.intake()
