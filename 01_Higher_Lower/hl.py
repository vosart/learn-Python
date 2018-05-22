# Project 01 Higher Lower
import random

print('Enter a digit 1-10: ')
result = True
pc_digit = random.randint(1, 10)

try:

    while result:
        user_digit = int(input())
        if user_digit > pc_digit:
            print('less')
        elif user_digit < pc_digit:
            print('more')
        else:
            print('BINGO!')
            result = False
except ValueError:
    print("It's not a digit")
input()
