import numpy as np
import matplotlib.pyplot as plt


class AnimatedColumn:
    # params:
    # ax where to render
    # array like [1, 0, 1, 0, 1, 1, 0] (view reference left --> top)
    def __init__(self, ax, row, col_index=0, motif_filled="o", motif_empty=","):
        # store params
        self.ax = ax
        self.row = row
        self.n = len(row)
        self.col_index = col_index

        # how to render motif
        self.motif_filled = motif_filled
        self.motif_empty = motif_empty

        # index row
        n = self.n
        self.line = np.array(
            [(self.row[i], n - i) for i in range(n)], 
            dtype=int
            )

        # split filled part and empty part according to motif
        # either 0 or 1
        self.filled_part = []
        self.empty_part = []

        for motif in self.line:
            point = (self.col_index, motif[1])

            if motif[0] == 1:
                self.filled_part.append(point)
            else:
                self.empty_part.append(point)

        # object to render
        self.scatter_filled, = self.ax.plot([0], [0], marker=self.motif_filled, linestyle='None', markerfacecolor='None', color="#1f77b4")
        self.scatter_empty, = self.ax.plot([1], [1], marker=self.motif_empty, linestyle='None', markerfacecolor='None', color="#1f77b4")
        return

    # i: index from top
    # j: index from bottom
    def render(self, i, j):
        # check if empty
        # select part to render
        # transpose then unpack to get x and y

        # for filled part
        if len(self.filled_part):
            data_filled_part = np.array(
                [point for point in self.filled_part if j <= point[1] <= i], 
                dtype=int
                )

            self.scatter_filled.set_data(*data_filled_part.T)

        # for empty part
        if len(self.empty_part):
            data_empty_part = np.array(
                [point for point in self.empty_part if j <= point[1] <= i], 
                dtype=int
                )

            self.scatter_empty.set_data(*data_empty_part.T)

        return self.scatter_filled, self.scatter_empty


# example
nb_rows = 10
line = [1 for i in range(nb_rows)]

# initialize fig and ax
fig, ax = plt.subplots()

# set up axis limits
ax.set_xlim([-1, 5])
ax.set_ylim([0, 2 * nb_rows + 1])

# create column to render
col = AnimatedColumn(ax, line, col_index=0)

# render (skip k from top and 3 from bottom)
col.render(5, 3)

plt.show()
