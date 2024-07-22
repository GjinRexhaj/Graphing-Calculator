# creates main window and sets gui as the output from qtDesigner
# contains custom signal/slot functions and their respective implementations

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import design_ui
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mplwidget import MplCanvas
from PySide6 import QtWidgets
import sys
import app_framework as framework

# create main window in accordance with pyuic generated content
class MyApp(QMainWindow, design_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalSlots()

    # connect custom slots/signals
    def connectSignalSlots(self):
        self.btn_graph.clicked.connect(self.graphFunction)
        self.lineEdit.returnPressed.connect(self.graphFunction)
        self.btn_clear.clicked.connect(self.clearGraph)
        self.actionAbout.triggered.connect(self.about)
        self.actionNew_Window.triggered.connect(self.new)
        self.actionSave_Image.triggered.connect(self.save)
        self.actionHelp.triggered.connect(self.help)

    # define custom signal functions
    def graphFunction(self):
        # TO-DO: catch exceptions
        print("graph function has been clicked!")
        textlineInput = self.lineEdit.text()
        MplCanvas.plot(textlineInput)

    def clearGraph(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Warning")
        dlg.setText("This action will clear all graph data.<p>Would you like to proceed?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
            print("graph has been cleared!")
            MplCanvas.clear(self)
        else:
            print("No!")


    # Actionbar implementation
    def about(self):
        about = QMessageBox(self)
        about.setWindowTitle("About")
        about.setText("Graphing Calculator<p>Version 0.6 (dev)<p>Built with PySide6<p>Created by: Gjin Rexhaj<p>github.com/gjinrexhaj")
        about.setStandardButtons(QMessageBox.Ok)
        about.setIcon(QMessageBox.Information)
        button = about.exec()
    
    def new(self):
        print('TO-DO: CREATE NEW WINDOW UPON INVOKATION OF THIS EVENT')

    def save(self):
        print('TO-DO: SAVE IMAGE UPON INVOKATION OF THIS EVENT')

    def help(self):
        help = QMessageBox(self)
        help.setWindowTitle("Help")
        help.setText("General Use:<p>Left-Click and drag to pan canvas. Scroll wheel up/down to zoom in/out.")
        help.setStandardButtons(QMessageBox.Ok)
        help.setIcon(QMessageBox.Information)
        button = help.exec()