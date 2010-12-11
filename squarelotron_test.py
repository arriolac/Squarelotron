""" 
    Program: test_squarelotron.py
    Author: Chris Arriola
    Date:   Dec. 9, 2010
    Description: Unit testing for squarelotron.py
"""
import squarelotron
import unittest

class TestSquarelotron(unittest.TestCase):

    def testMake_squarelotron(self):
        self.assertEquals([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12],
                           [13, 14, 15, 16]],
                          squarelotron.make_squarelotron(range(1,17)))

        self.assertEquals([[1, 2, 3, 4, 5],
                           [6, 7, 8, 9, 10],
                           [11, 12, 13, 14, 15],
                           [16, 17, 18, 19, 20],
                           [21, 22, 23, 24, 25]],
                          squarelotron.make_squarelotron(range(1,26)))
        
    def testMake_4x4_squarelotron(self):
        self.assertEquals([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12],
                           [13, 14, 15, 16]],
                          squarelotron.make_4x4_squarelotron())

    def testMake_5x5_squarelotron(self):
        self.assertEquals([[1, 2, 3, 4, 5],
                           [6, 7, 8, 9, 10],
                           [11, 12, 13, 14, 15],
                           [16, 17, 18, 19, 20],
                           [21, 22, 23, 24, 25]],
                          squarelotron.make_5x5_squarelotron())

    def testMake_list(self):
        self.assertEquals(
            range(1,17),
            squarelotron.make_list(squarelotron.make_4x4_squarelotron()))

        self.assertEquals(
            range(1,26),
            squarelotron.make_list(squarelotron.make_5x5_squarelotron()))
        
    def testUpside_down_flip(self):
        squarelotron_4x4 = squarelotron.make_4x4_squarelotron()
        squarelotron_5x5 = squarelotron.make_5x5_squarelotron()

        self.assertEquals(squarelotron.upside_down_flip(squarelotron_4x4, 0),
                          [[13, 14, 15, 16],
                           [9, 6, 7, 12],
                           [5, 10, 11, 8],
                           [1, 2, 3, 4]])
            

#        self.assertEquals(
#            [[1, 2, 3, 4],
#              [5, 10, 11, 8],
#              [9, 6, 7, 12],
#              [13, 14, 15, 16]],
#            squarelotron.upside_down_flip(squarelotron.make_4x4_squarelotron(), 1))

#        self.assertEquals(
#            [[[21, 22, 23, 24, 25],  
#              [16, 7, 8, 9, 21],
#              [11, 12, 13, 14, 15],
#              [6, 17, 18, 19, 10],
#              [1, 2, 3, 4, 5]],
#            squarelotron.upside_down_flip(squarelotron.make_5x5_squarelotron(), 0))
#
#        self.assertEquals(
#            [[[1, 2, 3, 4, 5],        
#              [6, 17, 18, 19, 10],
#              [11, 12, 13, 14, 15], 
#              [16, 7, 8, 9, 20],
#              [21, 22, 23, 24, 25]],
#            squarelotron.upside_down_flip(squarelotron.make_5x5_squarelotron(), 1))

#    def testLeft_right_flip(squarelotron, ring):
#        self.assertEquals(
#            [[4, 3, 2, 1],
#             [8, 6, 7, 5],
#             [12, 10, 11, 9],
#             [16, 15, 14, 13]],
#            squarelotron.left_right_flip(squarelotron.make_4x4_squarelotron(), 0))
#
#        self.assertEquals(
#            [[1, 2, 3, 4],
#              [5, 7, 6, 8],
#              [9, 11, 10, 12],
#              [13, 14, 15, 16]],
#            squarelotron.left_right_flip(squarelotron.make_4x4_squarelotron(), 1))
#
#        self.assertEquals(
#            [[[5, 4, 3, 2, 1],  
#              [10, 7, 8, 9, 6],
#              [15, 12, 13, 14, 11],
#              [20, 17, 18, 19, 16],
#              [25, 24, 23, 22, 21]],
#            squarelotron.left_right_flip(squarelotron.make_5x5_squarelotron(), 0))
#
#        self.assertEquals(
#            [[[1, 2, 3, 4, 5],        
#              [6, 9, 8, 7, 10],
#              [11, 14, 13, 12, 15], 
#              [16, 19, 18, 17, 20],
#              [21, 22, 23, 24, 25]],
#            squarelotron.left_right_flip(squarelotron.make_5x5_squarelotron(), 1))
            
unittest.main()
