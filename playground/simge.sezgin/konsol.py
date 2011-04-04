#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
from PyQt4 import QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QShortcut
import QTermWidget
from PyQt4.QtCore import QThread
def close():
    QThread.sleep(10)
    w.hide()    



a = QtGui.QApplication(sys.argv)
w = QTermWidget.QTermWidget()
w.resize(500,500)

shortcut=QShortcut("c",w,close)

w.setColorScheme(3)
w.show()
sys.exit(a.exec_())
    




