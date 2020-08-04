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
    return sorted(data, key=lambda x: x[len(x)-1])


# takes the mean and std_dev of each column and appends the
def data_summary(data):
    summary = []
    # get statistics for each column
    for i in zip(*data):
        summary.append([stat.mean(i), stat.pstdev(i), len(i)-1])
    # remove stats for class because its not useful
    del (summary[-1])
    return summary


def sumarize_class(data):
    arr = []
    for i in range(len(data)-1):
        temp = []
        for j in data:
            if j[len(j)-1] == i:
                temp.append(j)
        if len(temp) != 0:
            arr.append(temp)

    # print(arr[0])
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
def calculate_class_probabilities(data, row):
    total_rows = len(data)
    probs = []
    cl = 0
    for i in data:
        # x = data[cl]
        # y = data[cl][0]
        # z = data[cl][0][8]
        probs.append(data[cl][0][2]/float(total_rows))
        for j in range(len(i)):
            mu, sigma, count = i[j]
            if sigma == 0:
                continue
            k = probs[cl]
            probs[cl] = k * gauss_dist(row[j], mu, sigma)
        cl += 1
    return probs


# Predict the class for a given row
def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    best_label, best_prob = None, -1
    cl = 0
    for i in probabilities:
        if best_label is None or i > best_prob:
            best_prob = i
            best_label = cl
        cl += 1
    return best_label


# Naive Bayes Algorithm
def naive_bayes(train, test):
    summarize = sumarize_class(train)
    predictions = list()
    for row in test:
        output = predict(summarize, row)
        predictions.append(output)
    return (predictions)

if __name__ == '__main__':
    data = generate_datas(20)
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

    # print(data)
    data = split_data_by_class(data)
    dat = sumarize_class(data)
    #print(dat)
    probabilities = calculate_class_probabilities(dat, data[0])
    pred = predict(dat, data[0])
    print(pred)
    # for i in range(len(data)):
    #     print(data[i])

    # print(gauss_dist(1.0, 1.0, 1.0))
    # print(gauss_dist(2.0, 1.0, 1.0))
    # print(gauss_dist(0.0, 1.0, 1.0))
