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
        self.btn_clear.setProperty('class','danger')
        self.btn_clear.clicked.connect(self.clearGraph)
        self.actionAbout.triggered.connect(self.about)
        self.actionSave_Image.triggered.connect(self.save)
        self.actionHelp.triggered.connect(self.help)

    # define custom signal functions #

    # graph function as specified in lineEdit
    def graphFunction(self):
        print("graph function has been clicked!")
        textlineInput = self.lineEdit.text()
        
        try:
            MplCanvas.plot(textlineInput)
        except:
            exception = QMessageBox(self)
            exception.setWindowTitle("Error")
            exception.setText("Error graphing function: INPUT FORMATTING ERROR.<p>Here's an example of a correctly formatted function:<p>5*x^3 + sin(3*x)")
            exception.setStandardButtons(QMessageBox.Ok)
            exception.setIcon(QMessageBox.Critical)
            button = exception.exec()

    # clear canvas of all plotted functions
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


    # Actionbar implementation #

    # implemented 'about' dialog
    def about(self):
        about = QMessageBox(self)
        about.setWindowTitle("About")
        about.setText("Graphing Calculator<p>Version 1.0.0. Built with PySide6. Developed by Gjin Rexhaj<p>github.com/gjinrexhaj")
        about.setStandardButtons(QMessageBox.Ok)
        about.setIcon(QMessageBox.Information)
        button = about.exec()

    # implemented 'save' function
    def save(self):
        MplCanvas.save_image(self)

    # implemented 'help' dialog
    def help(self):
        help = QMessageBox(self)
        help.setWindowTitle("Help")
        help.setText("General Use:<p>Left-Click and drag to pan canvas. Scroll wheel up/down to zoom in/out.")
        help.setStandardButtons(QMessageBox.Ok)
        help.setIcon(QMessageBox.Information)
        button = help.exec()