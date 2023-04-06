#!/usr/bin/python3
#Password Generator Project
import random
# a;phabet, numbers and symbols to be in password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
lenght = nr_letters + nr_symbols + nr_numbers

#easy
password = ""  #creates an empty string to store random characters. The random.choice function generates a random value from a list
for ch in range(0, nr_letters):
        password += random.choice(letters)
for ch in range(0, nr_symbols):
    password += random.choice(symbols)
for ch in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

#hard
password_list = [] #same as above but instead stores the random charcters in a list
for ch in range(0, nr_letters):
        password_list += random.choice(letters)
for ch in range(0, nr_symbols):
    password_list += random.choice(symbols)
for ch in range(0, nr_numbers):
    password_list += random.choice(numbers)
print(password_list)

random.shuffle(password_list) #shuffles the list
password = "" #converts list into a string and then print
for ch in password_list:
    password += ch
print(f"Your password is {password}")
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
