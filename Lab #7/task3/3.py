import json

filename ="data1.json"
myfile = open(filename,mode='w',encoding='utf-8')
print("Cоздание JSON файла завершено!\n")
close1={
    'name: ':"rubashka",
    'kol_shtuk:':5,
   
    }
close2={
    'name: ':"kurtka",
    'kol_shtuk:':10,
    
    }

myclose=[]
myclose.append(close1)
myclose.append(close2)

#--------------------------------save----------------------------
json.dump(myclose,myfile)
myfile.close()
print("Сохранение JSON файла завершено!\n")
#-----------------------------loadJson--------------------
myfile = open(filename,mode='r',encoding='utf-8')
json_data=json.load(myfile)
sum=0

for close in json_data:
    print("name: " + str(close['name: ']))
    print("kol_shtuk:" + str(close['kol_shtuk:']))
    sum = sum + float(close['kol_shtuk:'])
print("\n")    
print("--------------------------")  
print("kol_shtuk:",sum) 
print("--------------------------\n")

#-----------------------------------------------------------------------
filename ="data2.json"
myfile1 = open(filename,mode='w',encoding='utf-8')

close3={
    'name: ':"botinki",
    'kol_par:':3,
   
    }
close4={
    'name: ':"tufli",
    'kol_par:':7,
    
    }

myclose1=[]
myclose1.append(close3)
myclose1.append(close4)
   
#--------------------------------save----------------------------
json.dump(myclose1,myfile1)
myfile1.close()
#-----------------------------loadJson--------------------
myfile1 = open(filename,mode='r',encoding='utf-8')
json_data1=json.load(myfile1)

sum1=0
for close in json_data1:
    print("name: " + str(close['name: ']))
    print("kol_par:" + str(close['kol_par:']))
    sum1 = sum1+ float(close['kol_par:'])    
print("\n")
print("--------------------------")  
print("kol_par:",sum1) 
print("--------------------------\n") 

filename ="sum.json"
myfile2 = open(filename,mode='w',encoding='utf-8')

mysum=[]
mysum.append(sum)
mysum.append(sum1)
json.dump(mysum,myfile2)
print("Сохрание завершено! JSON файл находится в файлах проекта!\n")
myfile2.close()