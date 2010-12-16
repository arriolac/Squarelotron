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

# Returns the squarelotron as a flat list of numbers
def make_list(squarelotron):
    return [item for sublist in squarelotron for item in sublist]

# Returns the column of a 2D array
def get_column(array, col):
    result = []
    for row in array:
        result.append(row[col])
    return result

# Restores the ring of a squarelotron to it's previous values
def restore_ring(postsquarelotron, presquarelotron, ring):
    returnSquarelotron = []
    for row in postsquarelotron:
        returnSquarelotron.append(list(row))

    for i in range(0, len(presquarelotron)):
        if (ring == 0):
            if (i != 0 and i != len(presquarelotron)-1):
                returnSquarelotron[i][1:-1] = presquarelotron[i][1:-1]
        else:
            if (i == 0 or i == len(presquarelotron)-1):
                returnSquarelotron[i][:] = presquarelotron[i][:]
            else:
                returnSquarelotron[i][0] = presquarelotron[i][0]
                returnSquarelotron[i][-1] = presquarelotron[i][-1]
    return returnSquarelotron

# Performs an upsidedown flip - 0 is the outer ring, 1 is the inner ring
def upside_down_flip(squarelotron, ring):
    reversedSquarelotron = []
    
    for row in reversed(squarelotron):
        reversedSquarelotron.append(list(row)) # create a hard copy of the list

    return restore_ring(reversedSquarelotron, squarelotron, ring)

# Performs a left to right flip - 0 is the outer ring, 1 is the inner ring
def left_right_flip(squarelotron, ring):
    reversedSquarelotron = []

    for row in squarelotron:
        reversedSquarelotron.append(list(row))
        reversedSquarelotron[-1].reverse()

    return restore_ring(reversedSquarelotron, squarelotron, ring)

# Performs an inverse diagonal flip
def inverse_diagonal_flip(squarelotron, ring):
    flippedSquarelotron = []

    for i in range(0, len(squarelotron)):
        flippedSquarelotron.append(get_column(squarelotron, -1-i))
        flippedSquarelotron[-1].reverse()

    return restore_ring(flippedSquarelotron, squarelotron, ring)

# Performs a main diagonal flip
def main_diagonal_flip(squarelotron, ring):
    flippedSquarelotron = []
    
    for i in range(0, len(squarelotron)):
        flippedSquarelotron.append(get_column(squarelotron, i))

    return restore_ring(flippedSquarelotron, squarelotron, ring)



# Starts the program
def main():
    size = input('Would you like a 4x4 or a 5x5 squarelotron? Enter 4 or 5: ')
     
