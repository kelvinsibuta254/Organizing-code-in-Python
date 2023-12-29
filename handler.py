f= open('file.txt', 'r')
print(f.read())
f.close()

f= open('file.txt', 'w')
f.write('I love u')
f.close()

f= open('file.txt', 'w')
f.write('\nMy name is Kelvin')
f.close()

with open('file.txt', 'r') as w:
    print(w.read())