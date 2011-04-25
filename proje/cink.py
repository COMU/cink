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
#def tamekran():
  #  w.resize(2048,2048)
#def tam_ekran():
  #  w.showFullScreen()
#def normal_ekran():
  #  w.showNormal()
'aynı tuşu kullanarak konsolu büyütüp küçültme'
def ekran():
    if(w.isFullScreen()==False):
        w.showFullScreen()
    else:
        w.showNormal()

def kapama():
    w.close()
w.setColorScheme(2)

kisayol1=QShortcut("Alt+g",w,gri)
kisayol2=QShortcut("ALT+y",w,yesil)
kisayol3=QShortcut("ALT+s",w,sari)
# kisayol4=QShortcut("SHIFT+CTRL+F11",w,tamekran)
kisayol6=QShortcut("Ctrl+F11",w,ekran)
kapat=QShortcut("ALT+c",w,kapama)

w.setScrollBarPosition(2)

w.show()
a.exec_()
