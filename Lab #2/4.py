#4
print ("\nВведите строку:\n")
string = input()
print ("\nВведите слово для поиска:\n")
word = input()
if word in string.split():
    print("\nНайденное слово",": ",word,"\n")
else:
    print("\nТакого слова нет в строке!\n")