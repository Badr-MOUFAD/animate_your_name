import numpy as np
import matplotlib.pyplot as plt

from class_render_line import AnimatedColumn


# figure to plot

############################
############################
############################
############################
#######              #######
#######              #######
#######              #######
#######              #######
############################
############################
############################
############################


# init figure
fig, ax = plt.subplots()

# general setups
nb_cols = 28
nb_rows = 12

template_col_border = [1 for i in range(nb_rows)]
template_col_center = [1 for i in range(int(nb_rows / 3))] + [0 for i in range(int(nb_rows / 3))] + [1 for i in range(int(nb_rows / 3))]

# create columns
arr_cols = []
for i in range(nb_cols):
    if i < 7 or i >= 21:
        arr_cols.append(
            AnimatedColumn(ax, template_col_border, col_index=i)
        )
    else:
        arr_cols.append(
            AnimatedColumn(ax, template_col_center, col_index=i)
        )

# render cols
for col in arr_cols:
    col.render()


# set axis limits then show
ax.set_xlim([-5, nb_cols + 5])
ax.set_ylim([-4, nb_rows + 5])

plt.show()
