#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import Qt
import QTermWidget
from tane import *

while True:
    karakter = raw_input(u"çıkmak için 'c' ye basınız\n")
    if karakter == 'c':
        a = Qt.QApplication(sys.argv)
        w = QTermWidget.QTermWidget()

        
        w.show()
        a.exec_()
        break
    print "Tıklanan tuş: %s" % karakter
