from src.perceptron import Perceptron
from src import parser
from src.Digit import sliding_pixle

total_training = 5000

data = parser.generate_datas(int(5000 * 0.5))
train_perc = Perceptron(data, len(data[0]) - 1, 10)  # -1 to get rid of label
train_perc.init_weights()
trained_perc = []
for i in range(1):
    print("Running training", i)
    trained_perc = train_perc.update_w()
print(trained_perc)

total_digit_testing = 1000

test_items = parser.loadDataFile("./data/digitdata/trainingimages", total_digit_testing, 28, 28)
test_lab = parser.loadLabelsFile("./data/digitdata/traininglabels", total_digit_testing)
hit = 0
for i in range(total_digit_testing):
    phi = sliding_pixle(test_items[i].data)
    phi.insert(0, 1)
    f = []
    for num in range(10):
        f.append(sum(p * w for p, w in zip(phi, trained_perc[num])))
    print("Test", i, "result", f.index(max(f)), "key", test_lab[i])
    if f.index(max(f)) == test_lab[i]:
        hit += 1
print("Accuracy ", hit / total_digit_testing)
