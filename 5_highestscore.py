#!/usr/bin/python3
student_scores = input("Input a list of student scores\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
n = 1
for score in student_scores:
    if n <= len(student_scores) - 1:
        if score > student_scores[n]:
            maxi = score
        else:
            maxi = student_scores[n]
        n = n + 1
print(f"The highest score in the class is: {maxi}")
