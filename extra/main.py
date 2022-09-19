from extra.MovAvg import MovAvg
import numpy as np

# x = np.array(100)
# y = np.random.rand(100)
x = [*range(1, 11, 1)]
y = [*range(1, 11, 1)]

data = MovAvg(x, y, 3)
# data.draw_graph()
data.draw_mov_avg_graph()