print("Welcome to Love Calculator")
name1 = input("Enter first person's name\n")
name2 = input("Enter second person's name\n")
name = name1 + name2 
name = name.lower()
n = 0
n2 = 0
n += name.count("t")
n += name.count("r")
n += name.count("u")
n += name.count("e")
n2 += name.count("l")
n2 += name.count("o")
n2 += name.count("v")
n2 += name.count("e")

score = str(n) + str(n2)
final_score = int(score)
if final_score < 10 or final_score > 90:
 print(f"Your score is {final_score}, you go together like coke and mentos")
elif final_score >= 40 and  final_score <= 50:
 print(f"Your score is {final_score}, you are alright together")
else:
 print(f"Your score is {final_score}")
