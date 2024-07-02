# prototype plotting
from mpl_interactions import ioff, panhandler, zoom_factory
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

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

# temp func
x_values = np.linspace(-100, 100, 100000) # 100000 points between -100 and 100 
y_values = [] 

print('type in a mathematical function:')
expression = input()
x = symbols('x')
symp_function = sympify(expression)
f = lambdify(x, symp_function)

for x in x_values: 
    y_values.append(f(x))
plt.plot(np.array(x_values), np.array(y_values)) 


# show plot
plt.show()