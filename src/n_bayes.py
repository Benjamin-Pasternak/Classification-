from parser import generate_datas
from parser import gen_test_data
from parser import gen_test_lab
from parser import gen_train_lab
import statistics as stat
from math import pi
from math import sqrt
from math import exp


class naive_bayes:

    def __init__(self, train_num, test_num):
        self.data = generate_datas(train_num)
        self.trainL = elim(gen_train_lab(train_num))
        # self.trainL = elim(trainL)
        self.testD = gen_test_data(test_num)
        self.testL = gen_test_lab(test_num)

        self.pred = self.naive_b(self.data, self.testD, self.trainL)

    # organizes data by class variable (or lable)
    def split_data_by_class(self, data):
        return sorted(data, key=lambda x: x[len(x) - 1])

    # takes the mean and std_dev of each column and appends the
    def data_summary(self, data):
        summary = []
        # get statistics for each column
        for i in zip(*data):
            summary.append([stat.mean(i), stat.pstdev(i), len(i) - 1])
        # remove stats for class because its not useful
        del (summary[-1])
        return summary

    def sumarize_class(self, data):
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
            ret.append(self.data_summary(i))
        return ret

    # we will be using the gaussian distribution function for our calculation
    # note, mean = mu, stdev = sigma
    # GAUSSIAN DENSITY FUNCTION from: https://pdfs.semanticscholar.org/847e/bd95e45f7814da821dce99b4c7ee565220e9.pdf
    # f(xi,mu_ij,sigma_ij) = (1/(sigma_ij*sqrt(2pi)))*e^(((x-mu_ij)^2)/(2(sigma_ij)^2))
    # argmax(yi) = P(class)\prod(j=1)(m) function^^ shall yield the prediciton of lables
    def gauss_dist(self, x, mu, sigma):
        return (1 / (sqrt(2 * pi) * sigma)) * exp(-((x - mu) ** 2 / (2 * sigma ** 2)))

    # now we can calculate the class probabilities
    def calculate_class_probabilities(self, data, row):
        total_rows = len(data)
        probs = []
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
        return probs

    # Predict the class for a given row
    def predict(self, summaries, row, sim):
        probabilities = self.calculate_class_probabilities(summaries, row)
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
    def naive_b(self, train, test, trainL):
        summarize = self.sumarize_class(train)
        predictions = list()
        for row in test:
            output = self.predict(summarize, row, trainL)
            predictions.append(output)
        return (predictions)

    def success_rate(self, preds, actual):
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
    bayes = naive_bayes(4999, 999)
    print(f"The percent accuracy = {bayes.success_rate(bayes.pred, bayes.testL)} %")
