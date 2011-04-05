#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
from PyQt4.QtGui import QShortcut
import QTermWidget

a=Qt.QApplication(sys.argv)
w=QTermWidget.QTermWidget()

def sari():
    w.setColorScheme(3)
def gri():
    w.setColorScheme(1)
def yesil():
    w.setColorScheme(2)

w.setColorScheme(2)
kisayol1=QShortcut("Alt+g",w,gri)
kisayol2=QShortcut("ALT+y",w,yesil)
kisayol3=QShortcut("ALT+s",w,sari)
w.setScrollBarPosition(2)

w.show()
a.exec_()
