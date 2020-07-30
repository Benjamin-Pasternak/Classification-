import numpy as np
from sys import exit
import os
from numba import njit

"""
This data class can be used to house either the digit or the 
face, depends on the 
"""
class Data:

    """
    Data houses the data array with imported info
    height is the height of array = 28
    width is the width of the array = 28
    """
    def __init__(self, data, height, width):
        self.height = height
        self.width = width
        self.data = data

# if you want the blank spaces gone: x.decode('utf8').strip()
def read_lines(filename):
    with open(filename, 'rb') as f:
        lines = [x.decode('utf8')[:-1] for x in f.readlines()]
    #print(lines[:-1])
    return lines[:-1]

def loadDataFile(filename, n, width, height):
    """
    Reads n data images from a file and returns a list of Datum objects.

    (Return less then n items if the end of file is encountered).
    """
    DATUM_WIDTH = width
    DATUM_HEIGHT = height
    fin = read_lines(filename)
    fin.reverse()
    items = []
    for i in range(n):
        data = []
        for j in range(height):
            data.append(list(fin.pop()))

        # if len(data[0]) < DATUM_WIDTH - 1:
        #     # we encountered end of file...
        #     print("Truncating at %d examples (maximum)" % i)
        #     # items.append(Data(data, DATUM_WIDTH, DATUM_HEIGHT))
        #     break
        data = convert_data_numeric(data)
        items.append(Data(data, DATUM_WIDTH, DATUM_HEIGHT))
    return items


# @njit
# def convert_data_numeric(data):
#     ret = []
#     for i in range(28):
#         temp = [0]
#         for j in range(28):
#             temp.append(ascii_to_digit(data[i][j]))
#         ret.append(temp[1:])
#     return ret


def convert_data_numeric(data):
    ret = np.arange(784).reshape((28, 28))
    for i in range(28):
        for j in range(28):
            ret[i][j] = ascii_to_digit(data[i][j])
    return ret


def ascii_to_digit(ch):
    if ch is ' ':
        return 0
    elif ch is '+':
        return 1
    else:
        return 2



if __name__ == "__main__":
    items = loadDataFile("./data/digitdata/trainingimages", 2, 28, 28)
    #items[1].data = convert_data_numeric(items[1].data)
    for i in range(len(items[1].data)):
        print(items[1].data[i])











