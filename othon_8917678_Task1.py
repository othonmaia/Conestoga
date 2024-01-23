# Name: othon_8917678_Task1.py
# Author: Othon Nascimento Maia
# Date Created: January 17, 2024
# Date Last Modified: January 18, 2024
# Purpose:
# Write a program that will calculate the area and perimeter of a rectangle, 
# based on user's input for width and length for the rectangle

height = float(input ("Whats the height (in cm)?"))
width = float(input ("Whats the width (in cm)?"))
area = height * width
perimeter = 2 * (height + width)
print("The area of the rectangule is " +str (area) + " cm^2 and the perimeter is " + str(perimeter) + "cm")