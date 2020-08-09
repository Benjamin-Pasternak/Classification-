from random import uniform
from src.Digit import easy_features


class Perceptron:

    def __init__(self, training_data, features, classes):
        self.data = training_data
        self.features = features
        self.label = classes
        self.weights = [None] * classes
        for i in range(classes):
            self.weights[i] = [0] * (self.features + 1)

    # Or can just use 0 for each weight without calling this func
    def init_weights(self):
        for num in range(self.label):
            for feature in range(self.features):
                self.weights[num][feature] = uniform(0, 0.1)

    def update_w(self):
        miss = 0
        count = -1
        for x in self.data:
            count += 1
            phi = x[0:self.features]
            phi.insert(0, 1)
            label = x[-1]
            # plabel = -1

            # while True:
            f = []
            for i in range(self.label):
                f.append(sum(p * w for p, w in zip(phi, self.weights[i])))
            plabel = f.index(max(f))
            if plabel == label:
                # break
                continue
            miss += 1
            for j in range(self.features + 1):
                print(count)
                print(label, plabel, j, len(phi))
                self.weights[label][j] += phi[j]
                self.weights[plabel][j] -= phi[j]

        print("Error", miss)
        return self.weights

    def estimate_class(self, test_item):
        phi = easy_features(test_item.data)
        phi.insert(0, 1)
        f = []
        for num in range(self.label):
            f.append(sum(p * w for p, w in zip(phi, self.weights[num])))
        # print("Test result", f.index(max(f)), "key", test_label)
        return f.index(max(f))


if __name__ == "__main__":
    data = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    # For digit
    a = Perceptron(data, len(data[0]) - 2, 10)  # Need to take out x&y from center, otherwise ignored
    a.init_weights()
    trained_f = a.update_w()
    # Test goes here
