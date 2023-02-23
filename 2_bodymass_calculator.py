weight = int(input("What is your weight in kg? "))
height = float(input("What is your height in m? "))
body_mass = int(weight / height ** 2)
print("Your body mass is " + str(body_mass))
