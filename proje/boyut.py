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

w.resize(600,400)
w.setColorScheme(2)
w.setScrollBarPosition(2)
kisayol1=QShortcut("Alt+g",w,gri)
kisayol2=QShortcut("ALT+y",w,yesil)
kisayol3=QShortcut("ALT+s",w,sari) 
kapat=QShortcut("ALT+c",w,kapama)
kisayol4=QShortcut("SHIFT+a",w,tamekran)
         
w.setColorScheme(2) 

def eventFilter(self, obj, event):
    if event.type() == QEvent.KeyPress: 
        key = event.key()
        if key == c:
            if self.isFullScreen():
                self.resize(600,400)
            else:
                self.showFullScreen()
            return True
    return QWidget.eventFilter(self, obj,event)

    
w.show()
a.exec_()


