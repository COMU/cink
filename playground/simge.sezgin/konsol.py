#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
from PyQt4 import QtGui
from PyQt4.QtGui import QShortcut
import QTermWidget

def close():
    a.exit()

a = QtGui.QApplication(sys.argv)
w = QTermWidget.QTermWidget()
w.resize(500,500)
shortcut=QShortcut("c",w,close)

w.show()
sys.exit(a.exec_())
    


