from PySide6 import QtWidgets
import sys

# Local app_framework import
import app_framework as framework

# Create GUI app
app = QtWidgets.QApplication(sys.argv)
form = framework.MyApp()
form.show()
app.exec()