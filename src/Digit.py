import numpy as np
from sys import exit
import os
from numba import njit

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

    # xs = 0
    # ys = 0
    # for i in range(len(upper_l)):
    #     xs += upper_l[i][0]
    #     ys += upper_l[i][1]
    #
    # center_upper = [xs / len(upper_l), ys / len(upper_l)]
    #
    # xs = 0
    # ys = 0
    # for i in range(len(lower_l)):
    #     xs += lower_l[i][0]
    #     ys += lower_l[i][1]
    #
    # center_lower = [xs / len(lower_l), ys / len(lower_l)]
    #
    # upper_density = upperhalf / 748
    # lower_density = lowerhalf / 748

    return [upperhalf, lowerhalf, num0, num1, num2, transitions]  # , center_upper,


# finds number of ones and twos in each row/col kind of
def easy_features(data):
    one_in_x = [0] * len(data)
    two_in_x = [0] * len(data)
    one_in_y = [0] * len(data[0])
    two_in_y = [0] * len(data[0])
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == 1:
                one_in_x[x] += 1
                one_in_y[y] += 1
            if data[x][y] == 2:
                two_in_x[x] += 1
                two_in_y[y] += 1
    # print(len(one_in_x + two_in_x + one_in_y + two_in_y))
    return one_in_x + two_in_x + one_in_y + two_in_y


# finds number of ones/twoes in each diagonal going top left down to bottom right
def other_features(data):
    n_1_diagonal = []

    # diagonal from left
    x = 0
    for y in range(27):
        i, j = x, y
        count = 0
        while i <= 27 and j <= 27:
            if data[i][j] == 1 or data[i][j] == 2:
                count += 1
            i += 1
            j += 1
        n_1_diagonal.append(count)

    y = 0
    for x in range(1, 27):
        i, j = x, y
        count = 0
        while i <= 27 and j <= 27:
            if data[i][j] == 1 or data[i][j] == 2:
                count += 1
            i += 1
            j += 1
        n_1_diagonal.append(count)

    return n_1_diagonal


# find ratio between left and right
# find number of things
def feature3(data):
    every3 = []
    x = len(data)
    y = len(data[0])
    for i in range(len(data)):
        ct = 0
        for j in range(20):
            sum = 0
            for k in range(3):
                sum += data[i][ct]
                ct += 1
            every3.append(sum)

    return every3


@njit
def feature4(data):
    l = []
    for i in range(len(data[0])):
        count = 0
        for j in range(len(data) // 3):
            sums = 0
            for k in range(3):
                sums += data[count][i]
                count += 1
            l.append(sums)

    return l[1:]


def feature5(data):
    ret = [0]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 2:
                # print('soop')
                ret.append(1)
            else:
                ret.append(0)
    y = ret[1:]
    # print('poof')
    return ret[1:]


def islands_and_size(data):
    """all cells are initially unvisited"""
    visited = [[False for j in range(len(data[0]))] for i in range(len(data))]
    counters = []
    count = 0
    trues = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if visited[i][j] == False and data[i][j] == 1:
                dfs(data, i, j, visited)
                count = count_trues(visited)
                trues = count - trues
                counters.append(trues)
                trues = count
                count += 1
    return counters

def count_trues(visited):
    trues = 0
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] == True:
                trues += 1
    return trues

def is_valid(data, i, j, visited):
    return (0 <= i < len(data) and
            0 <= j < len(data[0]) and
            not visited[i][j] and data[i][j])


def dfs(data, i, j, visited):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[i][j] = True
    for k in range(8):
        if is_valid(data, i + rowNbr[k], j + colNbr[k], visited):
            dfs(data, i + rowNbr[k], j + colNbr[k], visited)

    # right = 0
    # left = 0
    # count = 0
    # count2 = 0
    # for i in range(len(data)):
    #     for j in range(len(data[0])):
    #         if j > len(data[0]) // 2:
    #             left += 1
    #         else:
    #             right += 1
    #
    #         if 24 <= i <= 40 and 16 <= j <= 41:
    #             count += 1
    #         else:
    #             count2 += 1
    #
    # return [right / left, left / right, left, right, count, count2, count / count2, count2 / count]


if __name__ == "__main__":
    data = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]

    s = islands_and_size(data)
    print(s)
