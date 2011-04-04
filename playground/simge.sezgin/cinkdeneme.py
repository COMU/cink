#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
from PyQt4.QtGui import QShortcut
import QTermWidget

a=Qt.QApplication(sys.argv)
w=QTermWidget.QTermWidget()

def gri():
    w.setColorScheme(1)
def yesil():
    w.setColorScheme(2)
def sari():
    w.setColorScheme(3)

kisayol1=QShortcut("g",w,gri)
kisayol2=QShortcut("y",w,yesil)
kisayol3=QShortcut("s",w,sari)
w.setScrollBarPosition(2)

w.show()
a.exec_()
