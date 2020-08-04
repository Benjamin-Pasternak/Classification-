from parser import generate_datas
# from Util import *
from operator import itemgetter
import statistics as stat
import pandas as pd
from math import pi
from math import sqrt
from math import exp


# organizes data by class variable (or lable)
def split_data_by_class(data):
    return sorted(data, key=lambda x: x[8])


# takes the mean and std_dev of each column and appends the
def data_summary(data):
    summary = []
    # get statistics for each column
    for i in zip(*data):
        summary.append([stat.mean(i), stat.pstdev(i), len(i)])
    # remove stats for class because its not useful
    del (summary[-1])
    return summary


def sumarize_class(data):
    arr = []
    for i in range(9):
        temp = []
        for j in data:
            if j[8] == i:
                temp.append(j)
        if len(temp) != 0:
            arr.append(temp)

    # arr = []
    # temp = []
    # i = 0
    # curr = 0
    # while i <= len(data):
    #     x = data[i][8]
    #     if data[i][8] == curr:
    #         temp.append(data[i])
    #         i+=1
    #     else:
    #         curr+=1
    #         arr.append(temp)
    #         temp = []

    print(len(arr))
    ret = []
    for i in arr:
        ret.append(data_summary(i))
    return ret


# we will be using the gaussian distribution function for our calculation
# note, mean = mu, stdev = sigma
# GAUSSIAN DENSITY FUNCTION from: https://pdfs.semanticscholar.org/847e/bd95e45f7814da821dce99b4c7ee565220e9.pdf
# f(xi,mu_ij,sigma_ij) = (1/(sigma_ij*sqrt(2pi)))*e^(((x-mu_ij)^2)/(2(sigma_ij)^2))
# argmax(yi) = P(class)\prod(j=1)(m) function^^ shall yield the prediciton of lables
def gauss_dist(x, mu, sigma):
    return (1 / (sqrt(2 * pi) * sigma)) * exp(-((x - mu) ** 2 / (2 * sigma ** 2)))


# now we can calculate the class probabilities
def calc_probabilities()
# def summarize_by_class(data):
#     separated = split_data_by_class(data)
#     summaries = dict()
#     for class_value, rows in separated.items():
#         summaries[class_value] = data_summary(rows)
#     return summaries


if __name__ == '__main__':
    # data = generate_datas(2)
    # data = [[3.393533211, 2.331273381, 0],
    #         [3.110073483, 1.781539638, 0],
    #         [1.343808831, 3.368360954, 0],
    #         [3.582294042, 4.67917911, 0],
    #         [2.280362439, 2.866990263, 0],
    #         [7.423436942, 4.696522875, 1],
    #         [5.745051997, 3.533989803, 1],
    #         [9.172168622, 2.511101045, 1],
    #         [7.792783481, 3.424088941, 1],
    #         [7.939820817, 0.791637231, 1]]
    # data = split_data_by_class(data)
    # dat = sumarize_class(data)
    # for i in range(len(data)):
    #     print(data[i])
    # print(dat)
    print(gauss_dist(1.0, 1.0, 1.0))
    print(gauss_dist(2.0, 1.0, 1.0))
    print(gauss_dist(0.0, 1.0, 1.0))
