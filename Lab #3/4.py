def power(a,s):
         m=a**s
         return m

i=20
s=1
print("\nПервое вхождение: cтепень = 1!")
while i<=100:
       a=int(input("\nВведите число: "))
       print(power(a,s))
       s=a
       print("\nНовая степень: ", s)