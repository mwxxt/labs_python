import re

inm = open("G:/My Drive/Study/Folders/Declarative Programming/Labs/Lab #7/task2/pary.txt", "r")
out = open('G:/My Drive/Study/Folders/Declarative Programming/Labs/Lab #7/task2/result.txt', 'a')
summ1 = 0
  
number = inm.read() 
number = re.findall(r'[+-]?\d+', number) 
number = [int(y) for y in number] 
  
for y in number:
    summ1 += y

out.write("Quantity: ") 
out.write(str(summ1))
print("Quantity: ") 
print(str(summ1))
inm.close()
out.close()