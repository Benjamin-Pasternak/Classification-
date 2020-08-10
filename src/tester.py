from src.perceptron import Perceptron
from src.parser import *
from random import randrange
from statistics import mean, pstdev

face = False
if face:
    class_num = 2
    total_training = 451
    total_testing = 150
else:
    class_num = 10
    total_training = 5000
    total_testing = 1000

# digit image dimension 28*28
# face image dimension 60*70
all_data = generate_datas(int(total_training), face)
testing_data = gen_test_data(total_testing, face)
testing_lab = gen_test_lab(total_testing, face)
print("Initialized...")
parts = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
for part in parts:
    accs = []
    for i in range(5):
        if part == 1:
            start = 0
        else:
            start = randrange(total_training - int(total_training * part))
        training_data = all_data[start:int(start + total_training * part)]

        train_perc = Perceptron(training_data, len(training_data[0]) - 1, class_num)  # -1 to get rid of label
        train_perc.init_weights()
        train_perc.update_w()

        acc = train_perc.estimate_class(testing_data, testing_lab, face)
        accs.append(acc)
    print("Accuracy for", part, accs)
    print(mean(accs), pstdev(accs))
