x = int(input("\nВведите число от 1 до 9: "))
if x<1 or x>9:
    print("\nНеверный ввод! Выход из программы!\n")
else:
    print("\nВведено число:",x)
    if x>=7 and x<=9:
        list = []
        for num in range(10):
            list.append(x+num)
            num=num+1
        
        print(list)