#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QShortcut
import QTermWidget
from PyQt4 import QtCore
from PyQt4 import Qt

class Ana(QTermWidget.QTermWidget):
    
    def __init__(self):
        super(Ana, self).__init__()

        self.resize(500,500)
        self.setWindowTitle('konsol')

    def mousePressEvent(self,event):
        print "aaa"
        if event.button() == QtCore.Qt.RightButton:
            print "oldu"

def kapatma():
    app.exit()



if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    widget = Ana()
   # widget = QTermWidget.QTermWidget()
   # widget.resize(500, 500)
   # widget.setWindowTitle('konsol')
    shortcut1=QShortcut("@",widget,kapatma)
    widget.setScrollBarPosition(2)
    widget.setColorScheme(2)

    widget.show()
    sys.exit(app.exec_())
