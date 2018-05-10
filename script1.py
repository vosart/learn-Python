b = '1101'
i = 0

while b != '':
    print('b = ', b)
    i = i * 2 + int(b[0])
    print('i = ', i)
    b = b[1:]

print(i)
input()
