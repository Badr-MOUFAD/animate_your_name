import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from class_render_col import AnimatedColumn


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
        i = 1
        for col in self.grid:
            self.animated_cols.append(
                AnimatedColumn(ax, col, col_index=i)
            )
            i += 1

        # add signature
        self.ax.text(0.5, -2.5, 'Made by passion,\nBadr MOUFAD')

        # set axis range to display grid
        self.auto_set_axis()
        return

    def render(self):
        for col in self.animated_cols:
            col.render()
        return

    # provide pathname to save animation as gif 
    # example of pathname "screenshots/grid_example.gif"
    def animate(self, pathname=None):
        def anim(k):
            # vars
            n = len(self.grid[0])
            m = len(self.animated_cols)
            # nb_cols = len(self.animated_cols)
            arr_renders = []
            
            # cols to animate for the first half
            # from left to right
            col_index = 0
            for col in self.animated_cols[:int(m / 2)]:
                # top down
                if col_index % 2 == 0:
                    j = n - k + col_index * n
                
                    # stop animating if col is rendered completely
                    if j == 0:
                        continue

                    # add to collection of col to render
                    arr_renders +=  [*col.render(j=j)]
                
                # bottom up
                if col_index % 2 == 1:
                    i = k - col_index * n

                    # add to collection of col to render
                    arr_renders +=  [*col.render(i=i)]
                    

                col_index += 1

            # cols to animate for the second half
            # from right to left
            col_index = 0
            for col in self.animated_cols[m:int(m / 2) - 1:-1]:
                # top down
                if col_index % 2 == 0:
                    j = n - k + col_index  * n
                
                    # stop animating if col is rendered completely
                    if j == 0:
                        continue

                    # add to collection of col to render
                    arr_renders +=  [*col.render(j=j)]
                
                # bottom up
                if col_index % 2 == 1:
                    i = k - col_index * n 

                    # add to collection of col to render
                    arr_renders +=  [*col.render(i=i)]

                col_index += 1

            return arr_renders

        # grid domensions
        nb_cols = len(self.animated_cols)
        n = len(self.grid[0])

        self.a = FuncAnimation(self.fig, anim, frames=range(n * nb_cols + 1), interval=10, repeat=False)

        # to save animation as gif in the specifyed location
        if pathname:
            self.a.save(pathname, writer='Pillow', fps=120)
        return

    def auto_set_axis(self):
        # grid dimensions 
        x_max = len(self.grid)
        y_max = len(self.grid[0])

        # margin
        margin_x = 4
        margin_y = 4

        # set axis range
        self.ax.set_xlim(-margin_x, x_max + margin_x)
        self.ax.set_ylim(-margin_y, y_max + margin_y)
        return

# for an example
# refer to example_usage.py
