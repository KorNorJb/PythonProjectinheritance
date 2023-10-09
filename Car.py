import math
class car:
    def __init__(self, carBrand, carModel):
        self.cB = carBrand
        self.cM = carModel
    def start(self):
         print(f"Запуск автомобиля марки {self.cB} модель {self.cM}")
class Volvo(car):
    def start(self):
        if (self.cB == 'Volvo'):
            print(f"Запуск автомобиля марки {self.cB} модель {self.cM}. Машина готова к движению")
class KIA(car):
    def start(self):
         if (self.cB == 'KIA'):
            print(f"Запуск автомобиля марки {self.cB} модель {self.cM}")
class Chevrolet(car):
    def start(self):
        if (self.cB == 'Chevrolet'):
            print(f"Запуск автомобиля марки {self.cB} модель {self.cM}")
class AUDI(car):
    def start(self):
         if (self.cB == 'AUDI'):
            print(f"Запуск автомобиля марки {self.cB} модель {self.cM}")
carBrand = str(input("Введите марку машины: "))
carModel = str(input("Введите модель машины: "))
values = KIA(carBrand, carModel)
values2 = Volvo(carBrand, carModel)
values3 = Chevrolet(carBrand, carModel)
values4 = AUDI(carBrand, carModel)
values.start()
values2.start()
values3.start()
values4.start()
