import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from class_render_line import AnimatedColumn


class AnimatedGrid:
    # params
    # fig, ax from subplots function
    # grid a N x M array
    def __init__(self, fig, ax, grid):
        # store params
        self.fig = fig
        self.ax = ax
        
        # transform grid (row_i --> col_i)
        self.grid = []
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            self.grid.append(col)
        
        # create animated cols
        self.animated_cols = []
        i = 0
        for col in self.grid:
            self.animated_cols.append(
                AnimatedColumn(ax, col, col_index=i)
            )
            i += 1
        
        return

    def render(self):
        for col in self.animated_cols:
            col.render()
        return

    def animate(self):
        def anim(k):
            # vars
            n = len(self.grid[0])
            nb_cols = len(self.animated_cols)
            arr_renders = []
            
            # cols to animate
            col_index = 0
            for col in self.animated_cols:
                j = n + col_index * nb_cols - k
                
                # stop animating if col is rendered completely
                if j == 0:
                    continue

                # add to collection of col to render
                arr_renders +=  [*col.render(j=j)]

                col_index += 1

            return arr_renders

        nb_cols = len(self.animated_cols)
        n = len(self.grid[0])

        self.a = FuncAnimation(self.fig, anim, frames=range(nb_cols * nb_cols + n + 1), interval=50, repeat=True)
        return


# example
# init fig
fig, ax = plt.subplots()

# grid to animate
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# init object
g = AnimatedGrid(fig=fig, ax=ax, grid=grid)

# animate
g.animate()

# show
# axis limits
ax.set_xlim(-1, 10 + 1)
ax.set_ylim(-1, 7 + 1)

plt.show()
