# creates main window and sets gui as the output from qtDesigner
# contains custom signal/slot functions and their respective implementations

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import design_ui
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mplwidget import MplCanvas

# create main window in accordance with pyuic generated content
class MyApp(QMainWindow, design_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalSlots()

    # connect custom slots/signals
    def connectSignalSlots(self):
        self.btn_graph.clicked.connect(self.graphFunction)
        self.btn_clear.clicked.connect(self.clearGraph)
        self.actionAbout.triggered.connect(self.about)
        self.actionNew_Window.triggered.connect(self.new)
        self.actionSave_Image.triggered.connect(self.save)
        self.actionHelp.triggered.connect(self.help)

    # define custom signal functions
    def graphFunction(self):
        # TO-DO: take in text input, convert into lambda, then graph
        print("graph function has been clicked!")
        textlineInput = self.lineEdit.text()
        MplCanvas.plot(textlineInput)

    def clearGraph(self):
        print("graph has been cleared!")
        MplCanvas.clear()

    # Actionbar implementation
    def about(self):
        QMessageBox.about(
            self,
            "About",
            "<p>PySide6 Graphing Calculator</p>"
            "<p>Version: 0.5 (dev)</p>"
            "<p>Developed by: Gjin Rexhaj</p>"
            "<p>github.com/gjinrexhaj</p>",
        )
    
    def new(self):
        print('TO-DO: CREATE NEW WINDOW UPON INVOKATION OF THIS EVENT')

    def save(self):
        print('TO-DO: SAVE IMAGE UPON INVOKATION OF THIS EVENT')

    def help(self):
        print('TO-DO: HELP DIALOG UPON INVOKATION OF THIS EVENT')



    #def plot_data(self):
    #    x=range(0,10)
    #    y=range(0,20,2)
        #self.plotWidget.canvas.ax.plot(x, y)
        #self.plotWidget.canvas.draw()