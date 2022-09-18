import matplotlib.pyplot
import numpy as np
import matplotlib as plt


class MovAvg:
    time_x = None
    data_y = None
    avg_window = None

    def __init__(self, time_x, data_y, avg_window):
        self.time_x = time_x
        self.data_y = data_y
        self.avg_window = avg_window

    def draw_mov_avg_graph(self):
        window = self.avg_window
        temp_data = self.data_y
        if np.mod(window, 2) == 0:
            window += 1
        hw = (window - 1)/2

        n = len(temp_data)
        result = np.zeros(n)
        result = temp_data

        for i in range(2, n):
            init_sum = 0
            if i <= hw:
                k1 = 1
                k2 = 2*i-1
                z = k2
            elif (i + hw) > n:
                k1 = i-n+i
                k2 = nz = k2-k1
            else:
                k1 = i - hw
                k2 = i + hw
                z = window

            for j in range(int(k1), int(k2)):
                init_sum += temp_data[j]
            result[i] = init_sum/z

        plt.pyplot.plot(temp_data, self.time_x)
        plt.pyplot.waitforbuttonpress(timeout=-1)

    def draw_graph(self):

        plt.pyplot.plot(self.data_y, self.time_x)
        plt.pyplot.waitforbuttonpress(timeout=-1)