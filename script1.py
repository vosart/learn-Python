print('Enter a binary digit: ')
b = input()
i = 0

while b != '':
    i = i * 2 + int(b[0])
    b = b[1:]
    
print('Decimal: ', i)
input()