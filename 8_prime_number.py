#!/usr/bin/python3
def prime_checker(number):
    prime = 0
    for num in range(2, number - 1):
        if number % num == 0:
            prime = 1
            break
    if prime == 1:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")
n = int(input("Check this number "))
prime_checker(number = n)
