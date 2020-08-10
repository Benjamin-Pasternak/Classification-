from perceptron import Perceptron
from n_bayes import naive_bayes
from parser import *
from random import randrange
import timeit
import tracemalloc


face = True
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
all_data = generate_datas(total_training, face)
all_label = gen_train_lab(total_training, face)
testing_data = gen_test_data(total_testing, face)
testing_lab = gen_test_lab(total_testing, face)
# print("Initialized...")

part = 1
# print(part)
if part == 1:
    startidx = 0
else:
    startidx = randrange(total_training - int(total_training * part))
training_data = all_data[startidx:int(startidx + total_training * part)]
training_lab = all_label[startidx:int(startidx + total_training * part)]

train_perc = Perceptron(training_data, len(training_data[0]) - 1, class_num)  # -1 to get rid of label

start = timeit.default_timer()
tracemalloc.start()

train_perc.update_w()

stop = timeit.default_timer()
memory = tracemalloc.get_traced_memory()
time = stop - start
tracemalloc.stop()

train_nbayes = naive_bayes(training_data, training_lab, testing_data, testing_lab)

# print("n_bayes")
# print('Time Taken: {}s'.format(train_nbayes.time))
# print(f"Memory usage is {train_nbayes.memory[0] / 10**6}MB; Peak was {train_nbayes.memory[1] / 10**6}MB")
# print("Accuracy", train_nbayes.success_rate())

acc = train_perc.estimate_class(testing_data, testing_lab)

# print("\nPerceptron")
# print('Time Taken: {}s'.format(time))
# print(f"Memory usage is {memory[0] / 10**6}MB; Peak was {memory[1] / 10**6}MB")
# print("Accuracy", acc)
# print(f"{acc}\t{format(time)}\t{memory[1] / 10**6}")

print(f"{train_nbayes.success_rate()}\t{format(train_nbayes.time)}\t{train_nbayes.memory[1] / 10**6}\t{acc}\t{format(time)}\t{memory[1] / 10**6}\t")
