def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
a = [str(i) for i in input("\nВведите предложение: ").split()]
a[-1]=reverse(a[-1])
a[0]=reverse(a[0])
print("\nРевертирование первого и последнего слова: ",a)