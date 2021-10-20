
print("\nОбщество в начале XXI века\n")
year=int(input("Введите Ваш возраст: "))
if year>=0 and year<=6:
    print("\nВам в детский сад!\n")
elif year>=7 and year<=18:
    print("\nВам в школу!\n")
elif year>=19 and year<=25:
    print("\nВам в профессиональное учебное заведение!\n")
elif year>=26 and year<=60:
    print("\nВам на работу!\n")
elif year>=61 and year<=120:
    print("\nВам предоставляется выбор.\n")
elif year<0 or year>120:
    print("\nОшибка! Это программа для людей!\n")