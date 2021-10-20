words = input("\nВведите строку: ")
words = words.replace(',', '').replace('.', '').replace('...', '').replace(':', '').replace('!', '').replace('?', '').replace(';', '').replace('-', '').replace(')', '').replace('(', '').replace('"', '')
words = words.split()
letter_counts = list(map(lambda x: len(x), words))
 
 
print()
print("\nСлово - ",words)
print("Длина - ",letter_counts,"\n")