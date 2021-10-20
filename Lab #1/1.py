x = int(input("\nВведите число от 1 до 9: "))
if x<1 or x>9:
    print("\nНеверный ввод! Выход из программы!\n")
else:
    print("\nВведено число:",x)
    if x<=3:
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
        print("\nВыведено 10 значений!\n")
    else:
        print("\nОшибка ввода!")