# The class Animals Dog and Cat
# Author Slava Grishin 
# version 05.12.2021
#---------------------
class Animals:
    def eat(self):
        pass
    def make_a_sound(self):
        print("Звук животных");
class Cat(Animals):
    def make_a_sound(self):
        print("Мяу-Мяу");
    def drop_everything(self):
        print("Вставайте хозяева я уронил все");
    def Use_Dish(self):
        print("Кот поел из миски");
class Dog(Animals):
    def Use_Dish(self):
        print("Пёс поел из миски");
    def make_a_sound(self):
        print("Гав-Гав");
    def the_need_to_walk(self):
        print("Хочу гулять Хозяин");
Jack = Dog()
Jack.make_a_sound()
Jack.the_need_to_walk()
Baks = Cat()
Baks.make_a_sound()
Baks.drop_everything()

class Dish(Animals):
    def Use_Dish(self):
        print("Животные поели из миски");
Jack.Use_Dish()
Baks.Use_Dish()
Dish = 100
Jack = 100
Baks = 100
if (Dish < 10 ):print("Миска пустая")
if (Jack > 10): print("Джек поел из миски")

