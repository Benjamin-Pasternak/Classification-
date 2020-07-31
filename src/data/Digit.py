import numpy as np
from sys import exit
import os

"""
1. average number of non-zero pixels
2. average number of zero pixels
3. ratio of non-zero to zero
4. max/min non-zero
5. max/min zero
"""

"""
The geometrical featues:

Number of black pixels in the window.
Position of the uppermost black pixel.
Position of the lowermost black pixel.
Deviation of the uppermost pixel.
Deviation of the lowermost pixel.
Pixel density between upper and lower contour.
Number of black-to-white transitions in vertical direction.
Center of gravity.
The second derivative of the moment in vertical direction.
"""
class feature_finder:


    def __init__(self, data ,uppermost, lowermost, leftmost, rightmost, density, center_of_mass, difference_in_mass,
                 average_zeros, average_ones, average_twos):
        self.uppermost =

    # the goal of this function is to go over all of the pixles once and collect all of the information that is relevent
    # in one pass
    def sliding_pixle(self, data):
        # collects the upper and lower half
        upperhalf = 0
        lowerhalf = 0
        uppermost = []
        lowermost = []
        # leftmost = []
        # rightmost = []
        allpoints = []
        num0 = 0
        num1 = 0
        num2 = 0
        # we want to count the number of 0-1or2 transitions
        transitions = 0
        for i in range(28):
            for j in range(28):

                """
                fills upperhalf and lowerhalf respectivly with points so that i 
                can do density calc probably make it so that
                """
                if i<=13 and (data[i][j] is '1' or data[i][j] is '2'):
                    upperhalf+=1
                    #upperhalf.append((i, j))
                elif i > 13 and (data[i][j] is '1' or data[i][j] is '2'):
                    lowerhalf+=1
                    #lowerhalf.append((i, j))

                """
                uppermost stores a tuple (i, j) so uppermost[1] stores j gets the uppermost 
                pixle and lower most pixle
                """
                if i < uppermost[1] and (data[i][j] is '1' or data[i][j] is '2'):
                    uppermost = data[i][j]
                if i > lowermost[1] and (data[i][j] is '1' or data[i][j] is '2'):
                    lowermost = data[i][j]

                """
                counts the number of 1s 2s and 0s respectivly
                """
                if data[i][j] is '1':
                    num1+=1
                elif data[i][j] is '2':
                    num2+=1
                elif data[i][j] is '0':
                    num0+=1

                """
                this adds to a list of all points that are not 0
                """
                if data[i][j] is '1' or data[i][j] is '2':
                    allpoints.append(data[i][j])


        return [upperhalf, lowerhalf, lowermost, uppermost, num0, num1, num2, allpoints]








