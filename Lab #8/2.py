import datetime
d=int(input("\nВведите день в формате Int: "))
m=int(input("\nВведите месяц в формате Int: "))
y=int(input("\nВведите год в формате Int: "))
x = datetime.date(y, m, d)
print("\nДень:",x.day)
print("Месяц:",x.month)
print("Год:",x.year,"\n")