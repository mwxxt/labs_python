class Number:
    num = 1

    def __init__(self, num):
        self.Number = (num)
        print("[Конструктор сработал]")

    def func1(self, num):
            s=input("\nВведите строку: ")
            n=int(input("\nВведите число повторов строки: "))
            print("\nЧисло повторов для строки:",n,"\n")
            for x in range(n):
                print(s,"\n")

    def func2(self, num):
            m=int(input("\nВведите степень для данного числа: "))
            print("\nВведённое число в степени ",m," = ",num**m,"\n")

    def func3(self, num):
            for x in range(10):
                print("\nВывод: ",num+x)
                x=x+1
            print("\nВыведено 10 значений!\n")

    def func4(self, num):
            print("\nНеверный ввод! Выход из программы!\n")

    def __del__(self, num):
        print("\n[Деструктор сработал]\n\n")


number = Number(1)
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
number.__del__(num)