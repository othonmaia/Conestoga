# Name: othon_8917678_Task2.py
# Author: Othon Nascimento Maia
# Date Created: January 17, 2024
# Date Last Modified: January 18, 2024
# Purpose:

#This program 
# 1- square; 2-rectangle; 3- circle
# Areas: 
# - Square: side^2
# - Rectangle: lenght *width
# - Circle: 3.1415 * radius ^2
# Perimeter
# - Square: 4*side
# - Rectangle: 2* (lenght+width)
# - Circle:  3.1415 * 2 * radius
loop = 1

while loop == 1:
    gf= int(input("Do you want to see the square(1), rectangle (2) or circle (3)?"))
    if gf ==1:
        side = float(input("What's the side of the square? "))
        area = side*side
        perimeter= 4*side
        print(" The perimeter is "+ str(perimeter) +" cm and the area is " + str(area) + " cm^2")
    elif gf == 2:
        lenght = float(input("What's the lenght of the square? "))
        width = float(input("What's the width of the square? "))
        area = lenght * width
        perimeter = 2 * (lenght + width)
        print(" The perimeter is "+ str(perimeter) +" cm and the area is " + str(area) + " cm^2")
    elif gf == 3:
        radius = float(input("What's the radius of the circle? "))
        area = float(3.1415 * radius * radius)
        area = round(area, 2)
        perimeter = float(3.1415 * 2 * radius)
        perimeter = round(perimeter, 2)
        print(" The perimeter is "+ str(perimeter) +" cm and the area is " + str(area) + " cm^2")
    else:
        print("Number not available")
    loop = int(input("What to do it again? 1 for Yes, 2 for No "))