import matplotlib.pyplot as plt
class Graph_Analysis():

    def __init__(self, data_x, data_y, window):
        self.data_x = data_x
        self.data_y = data_y
        self.window = window

    def build_graph(self):
        plt.plot(self.data_x, self.data_y)


path = ('D:\software-engineering\class_sample\data.txt')
data = []
with open(path) as f:
    for line in f:
        data.append([float(x) for x in line.split()])
data  = [x for l in data for x in l]
x = tuple(data[::2])
y = tuple(data[1::2])

Graph_1 = Graph_Analysis(x, y, 3)
Graph_1.build_graph()
