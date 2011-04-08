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
def tamekran():
    w.showFullScreen()
def eskiekran():
    w.showNormal()
def kapama():
    w.close()
def ekran():
    while(True):
        kisayol7=QShortcut("SHIFT+t",w,tamekran)
        i=1
        if(i==1):
            kisayol8=QShortcut("SHIFT+t",w,eskiekran)
            break


w.resize(600,400)
w.setColorScheme(2)
w.setScrollBarPosition(2)
kisayol1=QShortcut("Alt+g",w,gri)
kisayol2=QShortcut("ALT+y",w,yesil)
kisayol3=QShortcut("ALT+s",w,sari) 
kapat=QShortcut("ALT+c",w,kapama)
kisayol4=QShortcut("SHIFT+a",w,ekran)
# kisayol7=QShortcut("SHIFT+t",w,tamekran)
w.setColorScheme(2) 


w.show()
a.exec_()


