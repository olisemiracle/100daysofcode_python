#!/usr/bin/python3
student_heights = input("Input a list of student height\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
lenght = 0
add = 0
for n in student_heights:
    lenght = lenght + 1
    add = add + n
average = round(add / lenght)
print(average)
