
from abc import ABC, abstractmethod

class Person(ABC):
    year = 0


class Num(Person):
    @abstractmethod
    def func1(self, year):
            print("\nВам в детский сад!\n")

    @abstractmethod
    def func2(self, year):
            print("\nВам в школу!\n")

    @abstractmethod
    def func3(self, year):
            print("\nВам в профессиональное учебное заведение!\n")

    @abstractmethod
    def func4(self, year):
            print("\nВам на работу!\n")

    @abstractmethod
    def func5(self, year):
            print("\nВам давно пора на пенсию!\n")
    
    @abstractmethod
    def func6(self, year):
            for i in range(0,5):
                print("\nОшибка! Это программа для людей!\n")


class Advanced(Num):
    def __init__(self, year):
        self.Num = (0) 
        print("[Конструктор сработал]")

    def func1(self, year):
        super().func1(year)
    def func2(self, year):
        super().func2(year)
    def func3(self, year):
        super().func3(year)   
    def func4(self, year):
        super().func4(year)
    def func5(self, year):
        super().func5(year)
    def func6(self, year):
        super().func6(year)


age = Advanced(0)
print("\nОбщество в начале XXI века\n")
year=int(input("Введите Ваш возраст: "))
if year>=0 and year<=6:
    age.func1(year)
elif year>=7 and year<=18:
    age.func2(year)
elif year>=19 and year<=25:
    age.func3(year)
elif year>=26 and year<=60:
    age.func4(year)
elif year>=61 and year<=120:
    age.func5(year)
elif year<0 or year>120:
    age.func6(year)