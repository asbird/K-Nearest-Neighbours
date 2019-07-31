import numpy as np
import pdb
import matplotlib.pyplot as plt


def scatter_data_points(data):
    for dxd in data:
        for xxd,yxd in data[dxd]:
            plt.scatter(xxd,yxd,c=dxd,s=100)


def draw_pt_connections(point,data):
    # Connections from point to all of the points from data
    for xxd,yxd in data:
        plt.plot([point[0],xxd],[point[1],yxd], c='r', linewidth=1)
        plt.pause(0.01)
