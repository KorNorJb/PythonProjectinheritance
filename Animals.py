# pip install pyglet or pip3 install pyglet

import pyglet
class Animals:
    def __init__(self, animal):
        self.sound = animal
    def start(self):
         if (self.sound != 'Собака' or 'Кошка'):
            print(f"Жди апдейтов. Пока звука {self.sound} нету")
class Dog(Animals):
    def start(self):
        if (self.sound == 'Собака'):
            dog = pyglet.resource.media("dog.mp3")
            dog.play()
            pyglet.app.run()
class Cat(Animals):
    def start(self):
        if (self.sound == 'Кошка'):
            cat = pyglet.resource.media("cat.mp3")
            cat.play()
            pyglet.app.run()

animal = str(input("Кошка или собака? : "))
values = Dog(animal)
values2 = Cat(animal)
values3 = Animals(animal)
values.start()
values2.start()
values3.start()
