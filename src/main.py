from PySide6 import QtWidgets
import sys
import qt_material

# Local app_framework import
import app_framework as framework

# Create GUI app
app = QtWidgets.QApplication(sys.argv)
form = framework.MyApp()

# apply style sheet
qt_material.apply_stylesheet(app, theme='dark_teal.xml')


# run app
form.show()
app.exec()