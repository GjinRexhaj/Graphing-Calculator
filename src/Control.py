# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QWidget)

class Control(object):
    def setupUi(self, Control):
        if not Control.objectName():
            Control.setObjectName(u"Control")
        Control.resize(950, 710)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Control.sizePolicy().hasHeightForWidth())
        Control.setSizePolicy(sizePolicy)
        Control.setMaximumSize(QSize(950, 710))
        Control.setStyleSheet(u"")
        self.actionOpen = QAction(Control)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(Control)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(Control)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionNew_Window = QAction(Control)
        self.actionNew_Window.setObjectName(u"actionNew_Window")
        self.actionHelp = QAction(Control)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionOpen_2 = QAction(Control)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.actionNew_2 = QAction(Control)
        self.actionNew_2.setObjectName(u"actionNew_2")
        self.actionOpen_3 = QAction(Control)
        self.actionOpen_3.setObjectName(u"actionOpen_3")
        self.actionSave_2 = QAction(Control)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionSave_As_2 = QAction(Control)
        self.actionSave_As_2.setObjectName(u"actionSave_As_2")
        self.actionAbout = QAction(Control)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(Control)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.graphingFrame = QFrame(self.centralwidget)
        self.graphingFrame.setObjectName(u"graphingFrame")
        self.graphingFrame.setGeometry(QRect(320, 20, 601, 601))
        self.graphingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.graphingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.graphingCanvas = QWidget(self.graphingFrame)
        self.graphingCanvas.setObjectName(u"graphingCanvas")
        self.graphingCanvas.setEnabled(True)
        self.graphingCanvas.setGeometry(QRect(0, 0, 601, 601))
        self.graphingCanvas.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(285, 20, 31, 621))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 100, 261, 541))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 259, 539))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 70, 281, 31))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btn_createFunction = QPushButton(self.centralwidget)
        self.btn_createFunction.setObjectName(u"btn_createFunction")
        self.btn_createFunction.setGeometry(QRect(20, 20, 121, 51))
        self.btn_createFunction.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_createFunction.setAutoDefault(True)
        self.btn_graph = QPushButton(self.centralwidget)
        self.btn_graph.setObjectName(u"btn_graph")
        self.btn_graph.setGeometry(QRect(160, 20, 121, 51))
        self.btn_graph.setAutoDefault(True)
        self.btn_graph.setFlat(False)
        self.graphingProgress = QProgressBar(self.centralwidget)
        self.graphingProgress.setObjectName(u"graphingProgress")
        self.graphingProgress.setGeometry(QRect(320, 630, 601, 23))
        font = QFont()
        font.setBold(True)
        self.graphingProgress.setFont(font)
        self.graphingProgress.setValue(0)
        self.graphingProgress.setTextVisible(True)
        self.graphingProgress.setInvertedAppearance(False)
        Control.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Control)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        Control.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Control)
        self.statusbar.setObjectName(u"statusbar")
        Control.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFile.addAction(self.actionNew_2)
        self.menuFile.addAction(self.actionOpen_3)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionSave_As_2)
        self.menuInfo.addAction(self.actionHelp)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.actionAbout)

        self.retranslateUi(Control)

        self.btn_graph.setDefault(False)


        QMetaObject.connectSlotsByName(Control)
    # setupUi

    def retranslateUi(self, Control):
        Control.setWindowTitle(QCoreApplication.translate("Control", u"Python Graphing Calculator", None))
        self.actionOpen.setText(QCoreApplication.translate("Control", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("Control", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("Control", u"Save As", None))
        self.actionNew_Window.setText(QCoreApplication.translate("Control", u"New Window", None))
        self.actionHelp.setText(QCoreApplication.translate("Control", u"Help", None))
        self.actionOpen_2.setText(QCoreApplication.translate("Control", u"Open", None))
        self.actionNew_2.setText(QCoreApplication.translate("Control", u"New", None))
        self.actionOpen_3.setText(QCoreApplication.translate("Control", u"Open", None))
        self.actionSave_2.setText(QCoreApplication.translate("Control", u"Save", None))
        self.actionSave_As_2.setText(QCoreApplication.translate("Control", u"Save As", None))
        self.actionAbout.setText(QCoreApplication.translate("Control", u"About", None))
#if QT_CONFIG(tooltip)
        self.btn_createFunction.setToolTip(QCoreApplication.translate("Control", u"Click to create a new function", None))
#endif // QT_CONFIG(tooltip)
        self.btn_createFunction.setText(QCoreApplication.translate("Control", u"Create Function", None))
#if QT_CONFIG(tooltip)
        self.btn_graph.setToolTip(QCoreApplication.translate("Control", u"Click to graph current functions", None))
#endif // QT_CONFIG(tooltip)
        self.btn_graph.setText(QCoreApplication.translate("Control", u"Graph", None))
        self.menuFile.setTitle(QCoreApplication.translate("Control", u"File", None))
        self.menuInfo.setTitle(QCoreApplication.translate("Control", u"Info", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Control()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
