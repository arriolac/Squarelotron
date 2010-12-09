""" 
    Program: squarelotron.py
    Author: Chris Arriola
    Date:   Dec. 9, 2010
    Description: A squarelotron game. The program will ask you to whether to 
    use a 4x4 or 5x5 squarelotron, then the program will let you tell it which
    flips to perform. 
"""
import math


# Creates a squarelotron from a list
def make_squarelotron(lst):
    size = int(math.sqrt(len(lst)))
    returnL = []
    for i in range(0, len(lst), size):
        returnL.append(lst[i:i+size])
    return returnL

# Creates a 4x4 squarelatron
def make_4x4_squarelotron():
    return make_squarelotron(range(1,17))

# Creates a 5x5 squarelatron
def make_5x5_squarelotron():
    return make_squarelotron(range(1,26))

# Starts the program
def main():
    size = input('Would you like a 4x4 or a 5x5 squarelotron? Enter 4 or 5: ')
     
