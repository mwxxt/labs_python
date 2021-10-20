str=input("\nВведите строку: ")
word = str.split()     # преобразование строки в список слов по разделению пробелом

LongWord = 0

for i in range(1,len(word)):
    if len(word[LongWord]) < len(word[i]):
        LongWord = i

print("\nСамое длинное слово: ",word[LongWord],"\n")
