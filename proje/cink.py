#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
from PyQt4.QtGui import QShortcut
import QTermWidget

a = Qt.QApplication(sys.argv)
w = QTermWidget.QTermWidget()

def sari():
    w.setColorScheme(3)
def gri():
    w.setColorScheme(1)
def yesil():
    w.setColorScheme(2)
def tam_ekran():
    w.showFullScreen()
def normal_ekran():
    w.showNormal()

w.setColorScheme(2)
kisayol1=QShortcut("Alt+g",w,gri)
kisayol2=QShortcut("ALT+y",w,yesil)
kisayol3=QShortcut("ALT+s",w,sari)
kisayol5=QShortcut("Ctrl+f",w,tam_ekran)
kisayol6=QShortcut("Ctrl+n",w,normal_ekran)

w.setScrollBarPosition(2)

w.show()
a.exec_()
