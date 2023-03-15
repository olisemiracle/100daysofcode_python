#!/usr/bin/python3
row1 = ["😃", "😃", "😃"]
row2 = ["😃", "😃", "😃"]
row3 = ["😃", "😃", "😃"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Row 0 - 2 || Column 0 -2 \n")
position1 = int(position[0])
position2 = int(position[1])
map[position1][position2] = "X"
print(f"{row1}\n{row2}\n{row3}")
