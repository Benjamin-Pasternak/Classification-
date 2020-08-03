from parser import generate_datas
#from Util import *
from operator import itemgetter
import statistics as stat
import pandas as pd


# organizes data by class variable (or lable)
def split_data_by_class(data):
    return sorted(data, key=lambda x:x[8])



# takes the mean and std_dev of each column and appends the
def data_summary(data):
    summary = []
    # get statistics for each column
    for i in zip(*data):
        summary.append([stat.mean(i), stat.pstdev(i), len(i)])
    # remove stats for class because its not useful
    del(summary[-1])
    return summary
















if __name__ == '__main__':
    data = generate_datas(2)
    data = split_data_by_class(data)
    sum = data_summary(data)
    # for i in range(len(data)):
    #     print(data[i])
    print(sum)

