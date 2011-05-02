#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import Qt, QtCore

class mymainwindow(Qt.QMainWindow):
    def __init__(self):
        #QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnBottomHint)
        Qt.QMainWindow.__init__(self, None, QtCore.Qt.FramelessWindowHint)

app = Qt.QApplication(sys.argv)
mywindow = mymainwindow()
mywindow.show()
app.exec_()


