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


def sliding_pixle(data):
    # features = uperhalf,lower half, center of density of each, total 1 and 2, number 120 respectivly,
    # transitions between 0 - 1 (genious), peakes on left and right, vallies on right and left

    # number of 1s and 2s in upper half and lower half
    upperhalf = 0
    lowerhalf = 0

    # upper_l and lower_l count positions for the centroid claculation later on
    upper_l = []
    lower_l = []

    # center_upper and center_lower will be calculated by another function that finds the centroid of a list of
    # points
    # center_upper = []
    # center_lower = []

    # total number of 0 and 1 and 2s respectively
    num0 = 0
    num1 = 0
    num2 = 0

    # transition counters, might need to implement in a different function, tv stands for transition valley
    # tp stand for transition peak, there will be 4 2 for each side. These will count number of absolute
    # minimum/maximum appear within the image
    # tv_left = 0
    # tv_right = 0
    # tp_left = 0
    # tp_right = 0
    # rmax = []
    # rmin = []
    # lmax = []
    # lmin = []
    transitions = 0

    # upper and lower count the number of relevent points in the upper and lower half of the image respectivly
    # can be used to identify reletive density of image in upper and lower part
    upper = 0
    lower = 0

    one = False
    zero = True
    for i in range(28):
        for j in range(28):

            # this guy fills upper half and lowerhalf and also upper_l and lower_l
            if i <= 13 and (data[i][j] == 1 or data[i][j] == 2):
                upperhalf += 1
                upper_l.append([i, j])
            elif i > 13 and (data[i][j] == 1 or data[i][j] == 2):
                lowerhalf += 1
                lower_l.append([i, j])

            # this will num0 num1 num2
            if data[i][j] == 1:
                num1 += 1
            elif data[i][j] == 2:
                num2 += 1
            elif data[i][j] == 0:
                num0 += 1

            if data[i][j] == 1 or data[i][j] == 2 and one is False:
                one = True
                zero = False
            if data[i][j] == 0 and zero is False:
                one = False
                zero = True
                transitions += 1

    xs = 0
    ys = 0
    for i in range(len(upper_l)):
        xs += upper_l[i][0]
        ys += upper_l[i][1]

    center_upper = [xs / len(upper_l), ys / len(upper_l)]

    xs = 0
    ys = 0
    for i in range(len(lower_l)):
        xs += lower_l[i][0]
        ys += lower_l[i][1]

    center_lower = [xs / len(lower_l), ys / len(lower_l)]

    upper_density = upperhalf / 748
    lower_density = lowerhalf / 748

    return [upperhalf, lowerhalf, upper_density, lower_density, num0, num1, num2, transitions, center_upper,
            center_lower]

    # upper half

    #
    # uppermost = []
    # lowermost = []
    # # leftmost = []
    # # rightmost = []
    # allpoints = []
    # num0 = 0
    # num1 = 0
    # num2 = 0
    # # we want to count the number of 0-1or2 transitions
    # transitions = 0
    # for i in range(28):
    #     for j in range(28):
    #
    #         """
    #         fills upperhalf and lowerhalf respectivly with points so that i
    #         can do density calc probably make it so that
    #         """
    #         if i<=13 and (data[i][j] is '1' or data[i][j] is '2'):
    #             upperhalf+=1
    #             #upperhalf.append((i, j))
    #         elif i > 13 and (data[i][j] is '1' or data[i][j] is '2'):
    #             lowerhalf+=1
    #             #lowerhalf.append((i, j))
    #
    #         """
    #         uppermost stores a tuple (i, j) so uppermost[1] stores j gets the uppermost
    #         pixle and lower most pixle
    #         """
    #         if i < uppermost[1] and (data[i][j] is '1' or data[i][j] is '2'):
    #             uppermost = data[i][j]
    #         if i > lowermost[1] and (data[i][j] is '1' or data[i][j] is '2'):
    #             lowermost = data[i][j]
    #
    #         """
    #         counts the number of 1s 2s and 0s respectivly
    #         """
    #         if data[i][j] is '1':
    #             num1+=1
    #         elif data[i][j] is '2':
    #             num2+=1
    #         elif data[i][j] is '0':
    #             num0+=1
    #
    #         """
    #         this adds to a list of all points that are not 0
    #         """
    #         if data[i][j] is '1' or data[i][j] is '2':
    #             allpoints.append(data[i][j])
    #
    #
    # return [upperhalf, lowerhalf, lowermost, uppermost, num0, num1, num2, allpoints]
