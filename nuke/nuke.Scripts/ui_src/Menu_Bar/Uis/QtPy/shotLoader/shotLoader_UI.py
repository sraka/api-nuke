#!/usr/bin/env python
# coding=utf-8

import os
import sys
from Qt import QtCompat, QtWidgets, QtCore , QtGui
from Qt.QtCompat import *
from Qt.QtWidgets import *
from Qt.QtCore import *
from Qt.QtGui import *
from Qt import *

# Import the ui file path
fileDir = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(fileDir, "uic", "shotLoader.ui")
# ssFile = os.path.join(fileDir, "css", "style.stylesheet")
# with open(ssFile, 'r') as f:
#     ssdata = f.read()

class MainUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = QtCompat.loadUi(uiFile, self)

        self.setWindowTitle("Tool Name")
        self.setWindowIcon(QtGui.QIcon("icons/logo.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Plastique")
    MainWindow = MainUI()
    MainWindow.show()
    sys.exit(app.exec_())


