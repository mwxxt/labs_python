s = input("\nВведите строку: ")
l = len(s)
m = 0
ind = 0
count = 0
for i in range(l):
    if s[i] != ';':
        count += 1
    else:
        if count > m:
            m = count
            ind = i - count
        count = 0
 
if count > m:
    m = count
    ind = i - count + 1
 
print("\nСамое длинное слово через точку запятую:",s[ind:ind+m],"\n")