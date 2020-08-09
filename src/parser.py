import numpy as np
from Digit import *
from feature import *

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


def loadDataFile(filename, n, width, height, face):
    """
    Reads n data images from a file and returns a list of Datum objects.

    (Return less then n items if the end of file is encountered).
    """
    DATUM_WIDTH = width
    DATUM_HEIGHT = height
    fin = read_lines(filename)
    fin.reverse()
    x = fin[0]
    y = len(x)
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
        data = convert_data_numeric(data, face)
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


def convert_data_numeric(data, face):
    if not face:
        ret = np.arange(784).reshape((28, 28))
        for i in range(28):
            for j in range(28):
                ret[i][j] = ascii_to_digit(data[i][j])
    else:
        #ret = np.arange(4278).reshape((62, 69))
        ret = np.arange(4140).reshape((69, 60))
        #c = 0
        for i in range(69):
            for j in range(60):
                ret[i][j] = ascii_to_digit(data[i][j])
                # c+=1
                # print(c)
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

def generate_datas(n, face):
    if not face:
        items = loadDataFile("./data/digitdata/trainingimages", n, 28, 28, face)
        lab = loadLabelsFile("./data/digitdata/traininglabels", n)
    elif face:
        items = loadDataFile("./data/facedata/facedatatrain", n, 62, 69, face)
        lab = loadLabelsFile("./data/facedata/facedatatrainlabels", n)


    # there's probably a better way of doing this with a dataframe pandas
    data_for_pro = []
    for i in range(len(lab)):
        # temp = sliding_pixle(items[i].data)
        #temp = easy_features(items[i].data)
        temp = feature5(items[i].data)
        #temp.extend(other_features(items[i].data))
        #if face:
            #temp.extend(sliding_pixle(items[i].data))
            #temp.extend(feature3(items[i].data))
            #temp.extend(feature4(items[i].data))
            #temp.extend(feature5(items[i].data))
            #temp.extend(advancedFeaturesExtract(items[i].data))
            #temp.extend(islands_and_size(items[i].data))
        temp.append(lab[i])
        data_for_pro.append(temp)

    return data_for_pro

def gen_test_data(n, face):
    if not face:
        items = loadDataFile("./data/digitdata/testimages", n, 28, 28, face)
    else:
        items = loadDataFile("./data/facedata/facedatatest", n, 60, 70, face)


    data_for_pro = []
    for i in range(len(items)):
        #temp = easy_features(items[i].data)
        temp = feature5(items[i].data)
        #temp.extend(other_features(items[i].data))
        #if face:
            #temp.extend(sliding_pixle(items[i].data))
            #temp.extend(feature3(items[i].data))
            #temp.extend(feature4(items[i].data))
            #temp.extend(feature5(items[i].data))
            #temp.extend(advancedFeaturesExtract(items[i].data))
            #temp.extend(islands_and_size(items[i].data))
        data_for_pro.append(temp)
    return data_for_pro

def gen_test_lab(n, face):
    if not face:
        item = loadLabelsFile("./data/digitdata/testlabels", n)
    elif face:
        item = loadLabelsFile("./data/facedata/facedatatestlabels", n)
    return item

def gen_train_lab(n, face):
    if not face:
        item = loadLabelsFile("./data/digitdata/traininglabels", n)
    else:
        item = loadLabelsFile("./data/facedata/facedatatrainlabels", n)
    return item







if __name__ == "__main__":
    items = loadDataFile("./data/facedata/facedatatest", 2, 60, 70, True)
    lab = loadLabelsFile("./data/facedata/facedatatestlabels", 2)

    fet = feature6(items[0].data)
    #fet2 = islands_and_size(items[1].data)
    print(len(fet))
    # items = loadDataFile("./data/digitdata/trainingimages", 2, 28, 28)
    # lab = loadLabelsFile("./data/digitdata/traininglabels", 2)

    # # there's probably a better way of doing this with a dataframe pandas
    # data_for_pro = []
    # for i in range(len(lab)):
    #     temp = easy_features(items[i].data)
    #     temp.append(lab[i])
    #     data_for_pro.append(temp)

    #print(data_for_pro[0])
    # ret = sliding_pixle(items[1].data)
    # print(ret)
    # items[1].data = convert_data_numeric(items[1].data)
    # for i in range(len(items[1].data)):
    #     print(items[1].data[i])
    # print(lab)
