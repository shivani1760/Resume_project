import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*"

upper, lower, num, symb = True, True, True, True
total = ""
if upper:
    total += uppercase_letters
if lower:
    total += lowercase_letters
if num:
    total += digits
if symb:
    total += symbols

length = input("Enter required characters length... ")
amount = input("Enter required amounts of passwords ... ")

for x in range(int(amount)):
    password = "".join(random.sample(total, int(length)))
    print(password)
