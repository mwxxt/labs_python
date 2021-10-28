import csv
csvreader = csv.reader(open("G:/My Drive/Study/Folders/Declarative Programming/Labs/Lab #7/task22/shtuki.cvs"),delimiter=' ')
reader = csv.reader(open("G:/My Drive/Study/Folders/Declarative Programming/Labs/Lab #7/task22/pary.cvs"),delimiter=' ')
out = open('G:/My Drive/Study/Folders/Declarative Programming/Labs/Lab #7/task22/result.cvs', 'a')
sum = 0
sum1 = 0
for row in csvreader:
    print(row)
    sum = sum + int(row[2])
for row in reader:
    print(row)
    sum1 = sum1 + int(row[2]) 
print("\nShtuki:",sum)
print("Pary:",sum1)
out.write("Shtuki: ")
out.write(str(sum))
out.write("Pary: ") 
out.write(str(sum1))
out.close()