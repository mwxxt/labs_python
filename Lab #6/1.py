from abc import ABC, abstractmethod

class Number(ABC):
    num = 0

class Num(Number):
    @abstractmethod
    def func1(self, num):
            s=input("\nВведите строку: ")
            n=int(input("\nВведите число повторов строки: "))
            print("\nЧисло повторов для строки:",n,"\n")
            for x in range(n):
                print(s,"\n")

    @abstractmethod
    def func2(self, num):
            m=int(input("\nВведите степень для данного числа: "))
            print("\nВведённое число в степени ",m," = ",num**m,"\n")

    @abstractmethod
    def func3(self, num):
            for x in range(10):
                print("\nВывод: ",num+x)
                x=x+1
            print("\nВыведено 10 значений!\n")

    @abstractmethod
    def func4(self, num):
            print("\nНеверный ввод! Выход из программы!\n")



class Advanced(Num):
    def __init__(self, num):
        self.num = (0) 
        print("[Конструктор сработал]")

    def func1(self, num):
        super().func1(num)
    def func2(self, num):
        super().func2(num)
    def func3(self, num):
        super().func3(num)   
    def func4(self, num):
        super().func4(num)

number = Advanced(0)
num = int(input("\nВведите число от 1 до 9: "))
print("\nВведено число:",num)
if num>=1 and num<=3:
    number.func1(num)
elif num>=4 and num<=6:
    number.func2(num)
elif num>=7 and num<=9:
    number.func3(num)
elif num<1 or num>9:
    number.func4(num)