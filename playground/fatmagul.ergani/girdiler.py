#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import Qt
import QTermWidget

while True:
    a = raw_input (u"lütfen girmek için c ye basınız: ")
    if a=='c':
        a = Qt.QApplication(sys.argv)
        w = QTermWidget.QTermWidget()

        w.show()
        a.exec_()

        break

