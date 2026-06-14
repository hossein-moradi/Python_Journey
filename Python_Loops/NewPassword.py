# So this exercise is about a password creating
import random

# Variables:
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
# First we get the randoms into a list
password = []
# Then we just join somthing into it and we get the result
something = ''

# We get the inputs here, we ask how many the user wants and we put into our variables
print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

# So here we use the for loop and random functions to get random letters, numbers and symbols
for x in range(number_of_letters):
    password.append(random.choice(letters))

for y in range(number_of_symbols):
    password.append(random.choice(symbols))

for z in range(number_of_numbers):
    password.append(random.choice(numbers))

# Print the result
new_password = something.join(password)
print(f"Here is your new password: {new_password}")

