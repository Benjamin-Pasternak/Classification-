from parser import generate_datas
from parser import gen_test_data
from parser import gen_test_lab
from parser import gen_train_lab
import statistics as stat
from math import pi
from math import sqrt
from math import exp
import timeit
import tracemalloc
from math import log


# organizes data by class variable (or label)
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


# test_split kinda
def sumarize_class(data):#, dig):
    arr = []
    for i in range(len(data) - 1):
        temp = []
        for j in data:
            if j[len(j) - 1] == i:
                temp.append(j)
        if len(temp) != 0:
            arr.append(temp)
    #if dig:
    ret = []
    for i in arr:
        ret.append(data_summary(i))
    return ret
    # else:
    #     return arr


class naive_bayes:

    def __init__(self, training_data, training_lab, test_data, test_lab):
        self.data = training_data
        self.trainL = elim(training_lab)
        self.testD = test_data
        self.testL = test_lab

        self.time = None
        self.memory = None

        self.pred = self.naive_b(self.data, self.testD, self.trainL)

    # we will be using the gaussian distribution function for our calculation
    # note, mean = mu, stdev = sigma
    # GAUSSIAN DENSITY FUNCTION from: https://pdfs.semanticscholar.org/847e/bd95e45f7814da821dce99b4c7ee565220e9.pdf
    # f(xi,mu_ij,sigma_ij) = (1/(sigma_ij*sqrt(2pi)))*e^(((x-mu_ij)^2)/(2(sigma_ij)^2))
    # argmax(yi) = P(class)\prod(j=1)(m) function^^ shall yield the prediciton of lables
    @staticmethod
    def gauss_dist(x, mu, sigma):
        return (1 / (sqrt(2 * pi) * sigma)) * exp(-((x - mu) ** 2 / (2 * sigma ** 2)))

    # this will yield p = Y/n where Y = sum(values)/num values
    # then we use Ylogp + (n-y)log(1-p) this will be our MLE
    # @staticmethod
    # def binomial_distribution(row, p):
    #     return 1
    # @staticmethod
    # def p_calc(data):
    #     for i in range(len(data[0])):



    # return sum(row)*log(p) + (len(row)-sum(row))*log(1-p)

    # now we can calculate the class probabilities
    def calculate_class_probabilities(self, data, row):#, dig):
        total_rows = len(data)
        probs = []
        #if dig:
        cl = 0
        for i in data:
            probs.append(data[cl][0][2] / float(total_rows))
            for j in range(len(i)):
                mu, sigma, count = i[j]
                if sigma == 0:
                    continue
                k = probs[cl]
                probs[cl] = k * self.gauss_dist(row[j], mu, sigma)
            cl += 1
            # print(probs)
        # else:
        #     # in order to find the p that maximizes our pdf is to take its first derivitive and set = 0
        #     p = p_calc(data)
        #     # since there are not 10 classes but 2
        #     for i in range(2):
        #         for j in range()
        return probs

    # Predict the class for a given row
    def predict(self, summaries, row, sim):#, dig):
        probabilities = self.calculate_class_probabilities(summaries, row)#, dig)
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
    def naive_b(self, train, test, trainL):#, dig):

        start = timeit.default_timer()
        tracemalloc.start()

        summarize = sumarize_class(train)#, dig)

        stop = timeit.default_timer()
        self.memory = tracemalloc.get_traced_memory()
        self.time = stop - start
        tracemalloc.stop()

        predictions = list()
        for row in test:
            output = self.predict(summarize, row, trainL)#, dig)
            predictions.append(output)
        return predictions

    def success_rate(self):
        correct = 0
        for i in range(len(self.pred)):
            if self.pred[i] == self.testL[i]:
                correct += 1
        return correct / len(self.pred)


def adjust_len(summarize):
    max = 0
    for i in range(len(summarize)):
        if max<len(summarize[i]):
            max = len(summarize[i])

    for i in range(len(summarize)):
        to_add = max - len(summarize[i])
        if to_add != 0:
            for j in range(to_add):
                summarize[i].append(summarize[i][0])
    return summarize

def adjust_row(row, n):
    if len(row) < n:
        m = n - len(row)
        for i in range(m):
            row.append(0)
    return row



def elim(t):
    t = list(dict.fromkeys(t))
    t.sort()
    return t


if __name__ == '__main__':
    bayes = naive_bayes(451, 150, False)
    print(f"The percent accuracy = {success_rate(bayes.pred, bayes.testL)}")
