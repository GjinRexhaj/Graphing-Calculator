from PySide6 import QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from mpl_interactions import ioff, panhandler, zoom_factory

matplotlib.use('QT5Agg')

# implemented MplCanvas
class MplCanvas(FigureCanvas):
    def __init__(self):
        xmin, xmax, ymin, ymax = -10, 10, -10, 10

        fig, self.ax = plt.subplots(figsize=(10,10))
        super().__init__(fig)
        
        #make figure occupy as much space as possible
        fig.tight_layout()

        #make x and y axis scales equal
        self.ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1,ymax+1), aspect='equal')

        #create x and y axis
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')

        #remove old axis
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        # create grid
        plt.grid(color = 'blue', linewidth = 0.2)

        #zoom
        disconnect_zoom = zoom_factory(self.ax)

        # panning
        pan_handler = panhandler(fig)

        #FigureCanvas.__init__(self, self.fig)
        #FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)