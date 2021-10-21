class Person:
    year = 1

    def __init__(self, year):
        self.Person = (year)
        print("[Конструктор сработал]")

    def func1(self,year):
        print("\nВам в детский сад!\n")

    def func2(self,year):
        print("\nВам в школу!\n")

    def func3(self,year):
        print("\nВам в профессиональное учебное заведение!\n")

    def func4(self,year):
        print("\nВам на работу!\n")

    def func5(self,year):
        print("\nВам давно пора на пенсию!\n")

    def func6(self,year):
        for i in range(0,5):
            print("\nОшибка! Это программа для людей!\n")

    def __del__(self,year):
        print("\n[Деструктор сработал]\n\n")


age = Person(1)
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
age.__del__(year)