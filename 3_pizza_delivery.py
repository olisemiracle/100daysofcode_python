print("Welcome to pizza deliveries")
size = input("What size of pizza do you want? S, M OR L\n")
if size == "S":
 pay = 15
 print("Small pizza: $15")
elif size == "M":
 pay = 20
 print("Medium pizza: $20")
else:
 pay = 25
 print("Large pizza: $25")
pep = input("Do you want pepperoni? Y or N\n")
if pep == "Y":
 if pay == 15:
  pay += 2
 else:
  pay += 3
cheese = input("Do you want extra cheese? Y or N\n")
if cheese == "Y":
 pay += 1
print(f"Your final bill is ${pay}")
