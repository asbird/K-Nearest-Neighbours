import numpy as np
import pdb
import matplotlib.pyplot as plt
import time

def main():
    data = {'y':[[1,1],[1,2],[2,1],[1,0]], 'b':[[5,4],[5,5],[4,5],[6,1]]}
    point = [1.5,4]

    fig = plt.figure()
    plt.scatter(point[0],point[1],c='g')
    scatter_data_points(data)
    draw_pt_connections(point,data)
    scatter_data_points(data)

    fig.clf()
    fig.show()




def scatter_data_points(data):
    for dxd in data:
        for xxd,yxd in data[dxd]:
            plt.scatter(xxd,yxd,c=dxd,s=100)


def draw_pt_connections(point,data):
    time.sleep(1)
    for xxd,yxd in data:
        plt.plot([point[0],xxd],[point[1],yxd], c='r', linewidth=1)
        plt.pause(0.3)


    # pdb.set_trace()

if __name__ == '__main__':
    main()
