def func(x):
    if x<1 or x>9:
        print("\nНеверный ввод!\n")
        return x

x = int(input("\nВведите число от 1 до 9: "))
print("\nВведено число:",x)
func(x)
if x<=3 and x>=1:
    s=input("\nВведите строку: ")
    n=int(input("\nВведите число повторов строки: "))
    print("\nЧисло повторов для строки:",n,"\n")
    for x in range(n):
        print(s,"\n")
elif x>=4 and x<=6:
        m=int(input("\nВведите степень для данного числа: "))
        print("\nВведённое число в степени ",m," = ",x**m,"\n")
elif x>=7 and x<=9:
    for num in range(10):
        print("\nВывод: ",x+num)
        num=num+1


def func(x):
    if year<0 or year>120:
        for i in range(0,5):
            print("\nОшибка! Это программа для людей!\n")

print("\nОбщество в начале XXI века\n")
year=int(input("Введите Ваш возраст: "))
func(year)
if year>=0 and year<=6:
    print("\nВам в детский сад!\n")
elif year>=7 and year<=18:
    print("\nВам в школу!\n")
elif year>=19 and year<=25:
    print("\nВам в профессиональное учебное заведение!\n")
elif year>=26 and year<=60:
    print("\nВам на работу!\n")
elif year>=61 and year<=120:
    print("\nВам давно пора на пенсию!\n")