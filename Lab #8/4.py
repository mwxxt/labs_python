import datetime
b=int(input("\nВведите год: "))
t=int(input("Введите месяц: "))
a=int(input("Введите день: "))
d = datetime.date(b, t, a)
print("\nВведённая дата:")
print("Год",b,"Месяц",t,"День",a)
print("\nОтвет после определённых вычислений:")
print("Год",d.year+1,"Месяц",d.month-1,"День",d.day,"\n")