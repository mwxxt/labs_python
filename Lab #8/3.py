
import datetime
r = str(input("\nВведите значения для даты: "))
a = r.split()
y=int(a[0])
m=int(a[1])
d=int(a[2])
day = datetime.date(y, m, d)
print("\nГод:",day.year)
print("Месяц:",day.month)
print("День:",day.day,"\n")