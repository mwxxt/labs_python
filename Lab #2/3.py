s = input("\nВведите строку: ")
l = len(s)
z = input("\nВведите знак разделения: ")
m = 50
ind = 0
count = 0
for i in range(l):
    if s[i] != z:
        count += 1
    else:
        if count < m:
            m = count
            ind = i - count
        count = 0
 
if count < m:
    m = count
    ind = i - count + 1
 
print("\nСамое короткое слово через введённый знак:",s[ind:ind+m],"\n")