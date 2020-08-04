from parser import generate_datas
from parser import gen_test_data
from parser import gen_test_lab
from parser import gen_train_lab
# from Util import *
from operator import itemgetter
import statistics as stat
import pandas as pd
from math import pi
from math import sqrt
from math import exp


# organizes data by class variable (or lable)
def split_data_by_class(data):
    return sorted(data, key=lambda x: x[len(x) - 1])


# takes the mean and std_dev of each column and appends the
def data_summary(data):
    summary = []
    # get statistics for each column
    for i in zip(*data):
        summary.append([stat.mean(i), stat.pstdev(i), len(i) - 1])
    # remove stats for class because its not useful
    del (summary[-1])
    return summary


def sumarize_class(data):
    arr = []
    for i in range(len(data) - 1):
        temp = []
        for j in data:
            if j[len(j) - 1] == i:
                temp.append(j)
        if len(temp) != 0:
            arr.append(temp)

    # print(arr[0])
    ret = []
    for i in arr:
        ret.append(data_summary(i))
    return ret


# note prior is a constant i believe. there are 10 classes 0...9 so 1/10
# Would it be (# at the position)/28  or  (# at the position)/112. Or (# at the position)/sum(values in list)
def liklihood_clac(x):
    return ((1 / x) * (1 / 10)) / (1 / 10)


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
        probs.append(data[cl][0][2] / float(total_rows))
        for j in range(len(i)):
            mu, sigma, count = i[j]
            if sigma == 0:
                continue
            k = probs[cl]
            probs[cl] = k * gauss_dist(row[j], mu, sigma)
        cl += 1
    # print(probs)
    return probs


# Predict the class for a given row
def predict(summaries, row, sim):
    probabilities = calculate_class_probabilities(summaries, row)
    # print(probabilities)
    best_label, best_prob = None, -1
    cl = 0
    for i in probabilities:
        if best_label is None or i > best_prob:
            best_prob = i
            best_label = sim[cl]
        cl += 1
    return best_label


# Naive Bayes Algorithm
def naive_bayes(train, test, trainL):
    summarize = sumarize_class(train)
    predictions = list()
    for row in test:
        output = predict(summarize, row, trainL)
        predictions.append(output)
    return (predictions)


def success_rate(preds, actual):
    correct = 0
    for i in range(len(preds)):
        if preds[i] == actual[i]:
            correct += 1
    return (correct / len(preds)) * 100


def elim(t):
    t = list(dict.fromkeys(t))
    t.sort()
    return t


if __name__ == '__main__':
    data = generate_datas(300)
    testD = gen_test_data(100)
    testL = gen_test_lab(100)
    trainL = gen_train_lab(300)
    trainL = elim(trainL)
    print(trainL)
    pred = naive_bayes(data, testD, trainL)
    print(naive_bayes(data, testD, trainL))
    print(testL)
    print(success_rate(pred, testL))

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
    # data = split_data_by_class(data)
    # dat = sumarize_class(data)
    # print(dat)
    # probabilities = calculate_class_probabilities(dat, data[0])
    # pred = predict(dat, data[0])
    # print(pred)
    # print(testD)

    # for i in range(len(data)):
    #     print(data[i])

    # print(gauss_dist(1.0, 1.0, 1.0))
    # print(gauss_dist(2.0, 1.0, 1.0))
    # print(gauss_dist(0.0, 1.0, 1.0))
