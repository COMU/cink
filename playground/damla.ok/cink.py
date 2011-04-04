#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
import QTermWidget

a = Qt.QApplication(sys.argv)
w = QTermWidget.QTermWidget()

w.setColorScheme(2)
w.setScrollBarPosition(2)
w.show()
a.exec_()
