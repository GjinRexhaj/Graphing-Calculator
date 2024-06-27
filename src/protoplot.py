# prototype plotting
from mpl_interactions import ioff, panhandler, zoom_factory
import numpy as np
import matplotlib.pyplot as plt

# set initial max x and y bounds
xmin, xmax, ymin, ymax = -10, 10, -10, 10
ticks_frequency = 1

# create figure, enable scroll to zoom
with plt.ioff():
    fig, ax = plt.subplots(figsize=(10,10))

#make x and y axis scales equal
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1,ymax+1), aspect='equal')

#create x and y axis
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

#remove old axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# create grid
plt.grid(color = 'blue', linewidth = 0.2)

#zoom
disconnect_zoom = zoom_factory(ax)

# panning
pan_handler = panhandler(fig)

# show plot
plt.show()