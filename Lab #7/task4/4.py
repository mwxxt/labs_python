import os
import json
open('textfile.json', 'tw', encoding='utf-8')
print(dir(os))
print(' ')
print(' ')
print('----------------------------------------------------------------------------')
print(' ')
print(' ')
print(os.getcwd())
print(' ')
print(' ')
print('----------------------------------------------------------------------------')
print(' ')
print(' ')
def list_files(startpath):  
   for root, dirs, files in os.walk(startpath):
       if dir!= '.git':
           level = root.replace(startpath, '').count(os.sep)
           indent = ' ' * 4 * (level)
           print('{}{}/'.format(indent, os.path.basename(root)))
           subindent = ' ' * 4 * (level + 1)
           for f in files:
               print('{}{}'.format(subindent, f))
startpath = os.getcwd()
list_files(startpath)
Fout = open ("textfile.json","w" ) 
Fout.write(startpath)