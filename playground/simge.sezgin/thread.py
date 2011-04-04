#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QThread
from time import sleep
from PyQt4.QtGui import QApplication
import QTermWidget
 
class Worker(QThread):
    print "hello" 
    def __init__(self): #thread oluştururken çalışacak, aynı süreçte.
        QThread.__init__(self)
    def run(self): #thread ayrı süreç içinde yapmasını istediğimiz şey.
        while True:
            print "+"
            sleep(10.0)

a=QtGui.QApplication(sys.argv)
widget=QTermWidget.QTermWidget()
w=Worker()
w.start() #bu fonksiyon, qthread'ın run fonksiyonunu ayrı bir süreç içinde çalıştırır
 
#ve kodumuz devam eder
 
while True:
    print "*"
    sleep(10.4)
