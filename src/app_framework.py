# creates main window and sets gui as the output from qtDesigner

from PySide6.QtWidgets import QApplication, QMainWindow
import design_ui

class MyApp(QMainWindow, design_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def plot_data(self):
        x=range(0,10)
        y=range(0,20,2)
        self.plotWidget.canvas.ax.plot(x, y)
        self.plotWidget.canvas.draw()