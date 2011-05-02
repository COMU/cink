#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
import QTermWidget
from PyQt4 import QtCore


a = Qt.QApplication(sys.argv)
w = QTermWidget.QTermWidget()
w.setColorScheme(2)
w.setScrollBarPosition(2)
#w.setWindowFlags(QtCore.Qt.SplashScreen)
#w.setWindowFlags(QtCore.Qt.SubWindow)
w.setWindowFlags(QtCore.Qt.FramelessWindowHint)


w.show()
a.exec_()
