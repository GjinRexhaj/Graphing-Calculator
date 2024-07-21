# mplwidget.py, creates zoom/pannable cartesian plane for graph widget

from PySide6 import QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from mpl_interactions import ioff, panhandler, zoom_factory
from sympy import lambdify, sympify, symbols
import qt_material

matplotlib.use('QT5Agg')

# implemented MplCanvas
class MplCanvas(FigureCanvas):

    # constructor
    def __init__(self):
        fig, self.ax = plt.subplots(figsize=(10,10))
        super().__init__(fig)
        
        xmin, xmax, ymin, ymax = -10, 10, -10, 10
        plt.ion()
        
        #make figure occupy as much space as possible
        fig.tight_layout()

        #change figure color
        fig.set_facecolor('#31363b')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')

        #make x and y axis scales equal
        self.ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1,ymax+1), aspect='equal')

        # plot axis lines
        plt.axhline(0, 0, 1, color='black')
        plt.axvline(0, 0, 1, color='black')

        #create x and y axis
        #self.ax.spines['bottom'].set_position('zero')
        #self.ax.spines['left'].set_position('zero')

        #remove old axis
        #self.ax.spines['top'].set_visible(False)
        #self.ax.spines['right'].set_visible(False)

        # create grid
        plt.grid(color = 'blue', linewidth = 0.2)

        #zoom
        #disconnect_zoom = zoom_factory(self.ax)
        zoom_factory(self.ax)

        # panning
        self.pan_handler = panhandler(fig)


    # plots input to graph, called by app_framework in graph button connected method
    def plot(input):
        print('input to be plot: ' + str(input))
        
        # temp func
        x_values = np.linspace(-1000, 1000, 100000) # 100000 points between -100 and 100 
        y_values = [] 

        # convert input into lambda
        # TO-DO, create seperate lambda_parser.py class with static lambda parser method
        # to process user input
        x = symbols('x')
        symp_function = sympify(input)
        f = lambdify(x, symp_function)

        for x in x_values: 
            y_values.append(f(x))
        plt.plot(np.array(x_values), np.array(y_values))
    
    # clear graph and apply cartesian plane to cleared plot
    def clear(self):
        
        print('internal clear method ran')
        plt.cla()
        plt.grid(color = 'blue', linewidth = 0.2)

        # plot axis lines
        plt.axhline(0, 0, 1, color='black')
        plt.axvline(0, 0, 1, color='black')


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    text = ''
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)