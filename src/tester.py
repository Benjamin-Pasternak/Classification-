from src.perceptron import Perceptron
from src import parser

total_training = 5000

data = parser.generate_datas(int(5000 * 0.5))
train_perc = Perceptron(data, len(data[0]) - 1, 10)  # -1 to get rid of label
train_perc.init_weights()
for i in range(1):
    print("Running training", i)
    trained_perc = train_perc.update_w()
    print(trained_perc)

total_digit_testing = 1000

test_items = parser.loadDataFile("./data/digitdata/trainingimages", total_digit_testing, 28, 28)
test_lab = parser.loadLabelsFile("./data/digitdata/traininglabels", total_digit_testing)
hit = 0
for i in range(total_digit_testing):
    result = train_perc.estimate_class(test_items[i], test_lab[i])
    if result == test_lab[i]:
        hit += 1
print("Accuracy ", hit / total_digit_testing)
