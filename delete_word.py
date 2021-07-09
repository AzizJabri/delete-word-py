import os
from sys import platform

def clear():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

def writing(txt):
    with open('output.txt', 'w') as outfile:
        outfile.write(txt)
    print('DONE !, check output.txt')


# keyword to stop reading words to delete
keyword = ' '

clear()

print('Type the text to delete words in :')
txt = str(input())
answer = ''
words = []

# reading words to censor
while answer != keyword:
    os.system('cls')
    print('Words To Delete (insert empty space to continue) :', ', '.join(words))
    answer = str(input())
    if answer != keyword:
        words.append(answer)


clear()

# replacing words
for i in words :
    text = txt.replace(i, '')
    txt = text

# deleting double spaces  
txt = " ".join(txt.split())

# uncomment this if you want the output printed to console :
print(txt)

# writing the text to output.txt (uncomment this if you want the text as a file 'output.txt')
#writing(txt)