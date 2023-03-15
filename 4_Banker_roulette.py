#!/usr/bin/python3
import random
names = input("Give me everybody's name seperated by comma\n")
names = names.split(", ")
num = len(names)
ran = random.randint(0, num - 1)
print(f"{names[ran]} gets to pay the bill")
