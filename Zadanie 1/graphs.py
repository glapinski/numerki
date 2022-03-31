import numpy as np
from matplotlib import pyplot as plt
from numpy import double
import funkcje as f


def graph(x, y, x0, flag):
    x_data = np.linspace(x, y, 1000)
    y_data = f.function(x_data, flag)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    if type(x0) == double:
        plt.plot(x0, 0, 'ro')
    plt.plot(x_data, y_data, 'g')
    plt.xlabel('X', loc='right')
    plt.ylabel('Y', loc='top')
    plt.title('Wykres')
    plt.show()
