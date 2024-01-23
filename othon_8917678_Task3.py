# Name: othon_8917678_Task3.py
# Author: Othon Nascimento Maia
# Date Created: January 17, 2024
# Date Last Modified: January 18, 2024
# Purpose:

# Length > 1: "Sorry, country name must be longer than one letter."
# Length < 21: "Sorry, country name cannot be more than 20 letters in length."
# Use trim() to get extra spaces before and after.
# Use while to loop.

loop = 1

while loop == 1:
    country = str(input("Type a country "))
    country = country.strip()
    length = len(country)
    end = length + 1
    if length <2:
        print("Sorry, country name must be longer than one letter.")
    elif length >20:
        print("Sorry, country name cannot be more than 20 letters in length.")
    else:
        print("Your country is " + str(country))
        loop = 2