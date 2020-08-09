from src.perceptron import Perceptron
from src import parser

total_digit_training = 5000
total_face_training = 451
# digit image dimension 28*28
# face image dimension 60*70
data = parser.generate_datas(int(total_face_training * 1), True)

train_perc = Perceptron(data, len(data[0]) - 1, 2)  # -1 to get rid of label
for i in range(1):
    print("Running training", i)
    trained_perc = train_perc.update_w()

total_digit_testing = 1000
total_face_testing = 150

test_items = parser.loadDataFile("./data/facedata/facedatatest", total_face_testing, 60, 70)
test_lab = parser.loadLabelsFile("./data/facedata/facedatatestlabels", total_face_testing)
hit = 0
for i in range(total_face_testing):
    result = train_perc.estimate_class(test_items[i], True)
    if result == test_lab[i]:
        hit += 1
print("Accuracy", hit / total_face_testing)
# digit easy feature only
# 0.422 0.469 0.588 0.512 0.622 0.619 0.590 0.593 0.550 0.627
# digit easy & other feature
# 0.438 0.358 0.382 0.474 0.463 0.464 0.551 0.428 0.402 0.538
