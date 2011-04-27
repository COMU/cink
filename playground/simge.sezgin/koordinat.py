#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import Qt
from PyQt4.QtGui import QShortcut
from QTermWidget import QTermWidget


class Center(QTermWidget):
    def __init__(self,parent=None):
        QTermWidget.__init__(self)
        self.center()
    'key press event eklemeyi dene' 

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 0)

    def artir(self):
        size =  self.geometry()
        en=size.width()
        boy=size.height()
        while(True):
            en=en+200
            boy=boy+400
            self.resize(en,boy)
            break



app= Qt.QApplication(sys.argv)
w = Center()
w.setScrollBarPosition(2)
w.show()
sys.exit(app.exec_())


