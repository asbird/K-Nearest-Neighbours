import numpy as np
import pdb
import matplotlib.pyplot as plt
from matplotlib import style
import time
import itertools
import math
import KNN_visualizations as KNNV

style.use('fivethirtyeight')


def main():
    data = {'y':[[1,1],[1,2],[2,1],[1,0]], 'b':[[5,4],[5,5],[4,5],[6,1]]}

    y = [1.5,3]
    fig = plt.figure()
    plt.scatter(y[0],y[1],c='g')
    KNNV.scatter_data_points(data)
    # pdb.set_trace()

    # We can mix values because one vector from all of the values stands for
    # one row of data in real dataframe so it's unique and has got it's own label
    dataList = list(itertools.chain.from_iterable(data.values()))
    print(dataList)
    asd = sorted(dataList, key=lambda pt: euclidean_temp(y, pt))
    KNNV.draw_pt_connections(y,asd[:3])
    plt.show()


def euclidean_temp(point, pt):
    sum = 0
    for q,p in zip(point, pt):
        sum+=(q-p)**2
    return math.sqrt(sum)

def check_key_of_point(point, dict):
    for group in dict:
        for pt in dict[group]:
            if point == pt:
                print(group)


if __name__ == '__main__':
    main()
