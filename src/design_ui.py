# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 669)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionNew_Window = QAction(MainWindow)
        self.actionNew_Window.setObjectName(u"actionNew_Window")
        self.actionSave_Image = QAction(MainWindow)
        self.actionSave_Image.setObjectName(u"actionSave_Image")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 3)

        self.graphingFrame = QFrame(self.centralwidget)
        self.graphingFrame.setObjectName(u"graphingFrame")
        self.graphingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.graphingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.graphingFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphingCanvas = MplWidget(self.graphingFrame)
        self.graphingCanvas.setObjectName(u"graphingCanvas")
        self.graphingCanvas.setEnabled(True)
        self.graphingCanvas.setCursor(QCursor(Qt.CursorShape.CrossCursor))

        self.gridLayout.addWidget(self.graphingCanvas, 0, 0, 1, 1)

        self.graphingProgress = QProgressBar(self.graphingFrame)
        self.graphingProgress.setObjectName(u"graphingProgress")
        font = QFont()
        font.setBold(True)
        self.graphingProgress.setFont(font)
        self.graphingProgress.setValue(0)
        self.graphingProgress.setTextVisible(True)
        self.graphingProgress.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.graphingProgress, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.graphingFrame, 2, 0, 1, 3)

        self.btn_createFunction = QPushButton(self.centralwidget)
        self.btn_createFunction.setObjectName(u"btn_createFunction")
        self.btn_createFunction.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_createFunction.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.btn_createFunction, 0, 0, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"")

        self.gridLayout_2.addWidget(self.btn_clear, 0, 2, 1, 1)

        self.btn_graph = QPushButton(self.centralwidget)
        self.btn_graph.setObjectName(u"btn_graph")
        self.btn_graph.setStyleSheet(u"background-color: rgb(87, 227, 137);")
        self.btn_graph.setAutoDefault(True)
        self.btn_graph.setFlat(False)

        self.gridLayout_2.addWidget(self.btn_graph, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Image)
        self.menuInfo.addAction(self.actionHelp)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.btn_createFunction.clicked.connect(self.lineEdit.clear)

        self.btn_graph.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionNew_Window.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionSave_Image.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter function here... (Example: x+5)", None))
#if QT_CONFIG(tooltip)
        self.btn_createFunction.setToolTip(QCoreApplication.translate("MainWindow", u"Click to create a new function", None))
#endif // QT_CONFIG(tooltip)
        self.btn_createFunction.setText(QCoreApplication.translate("MainWindow", u"New Function", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Graph", None))
#if QT_CONFIG(tooltip)
        self.btn_graph.setToolTip(QCoreApplication.translate("MainWindow", u"Click to graph current functions", None))
#endif // QT_CONFIG(tooltip)
        self.btn_graph.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

