import re 
  
inp = open("G:/My Drive/Study/Folders/Declarative Programming/Labs/Lab #7/task1/quantity.txt", "r")

out = open('G:/My Drive/Study/Folders/Declarative Programming/Labs/Lab #7/task1/result.txt', 'a')
summ = 0
  
numbers = inp.read() 
numbers = re.findall(r'[+-]?\d+', numbers) 
numbers = [int(x) for x in numbers] 
  
for x in numbers:
    summ += x

out.write("Quantity: ") 
out.write(str(summ))
print("Quantity: ") 
print(str(summ)) 