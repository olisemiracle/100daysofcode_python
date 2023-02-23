weight = int(input("What is your weight in kg?\n"))
height = float(input("What is your height in m?\n"))
body_mass = int(weight / height ** 2)
if body_mass < 18.5:
 print(f"Your body mass is {body_mass}, you are underweight")
elif body_mass < 25:
 print(f"Your body mass is {body_mass}, you are normal weight")
elif body_mass < 30:
 print(f"Your body mass is {body_mass}, you are overweight")
elif body_mass < 35:
 print(f"Your body mass is {body_mass}, you are obese")
else:
 print(f"Your body mass is {body_mass}, you are clinically obese")
