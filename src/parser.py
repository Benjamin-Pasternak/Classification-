import numpy as np
from src.Digit import *

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
        self.lables = []


# if you want the blank spaces gone: x.decode('utf8').strip()
def read_lines(filename):
    with open(filename, 'rb') as f:
        lines = [x.decode('utf8')[:-1] for x in f.readlines()]
    # print(lines[:-1])
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


def loadLabelsFile(filename, n):
    """
    Reads n labels from a file and returns a list of integers.
    """
    fin = read_lines(filename)
    labels = []
    for line in fin[:min(n, len(fin))]:
        if line == '':
            break
        labels.append(int(line))

    return labels

def generate_datas(n):
    items = loadDataFile("./data/digitdata/trainingimages", n, 28, 28)
    lab = loadLabelsFile("./data/digitdata/traininglabels", n)

    # there's probably a better way of doing this with a dataframe pandas
    data_for_pro = []
    for i in range(len(lab)):
        # temp = sliding_pixle(items[i].data)
        temp = easy_features(items[i].data)
        temp.append(lab[i])
        data_for_pro.append(temp)

    return data_for_pro



if __name__ == "__main__":
    items = loadDataFile("./data/digitdata/trainingimages", 2, 28, 28)
    lab = loadLabelsFile("./data/digitdata/traininglabels", 2)

    # there's probably a better way of doing this with a dataframe pandas
    data_for_pro = []
    for i in range(len(lab)):
        temp = easy_features(items[i].data)
        temp.append(lab[i])
        data_for_pro.append(temp)

    print(data_for_pro[0])
    # ret = sliding_pixle(items[1].data)
    # print(ret)
    # items[1].data = convert_data_numeric(items[1].data)
    # for i in range(len(items[1].data)):
    #     print(items[1].data[i])
    # print(lab)
