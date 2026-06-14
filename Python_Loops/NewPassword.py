# So this exercise is about a password creating

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7',
           '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*',
           '+']
password = []
print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

for x in range(number_of_letters):
    password.append(random.choice(letters))

for y in range(number_of_symbols):
    password.append(random.choices(symbols))

for z in range(number_of_numbers):
    password.append(random.choices(numbers))
print(password)







# print(numbers[number_of_symbols])
# print(numbers[number_of_numbers])
