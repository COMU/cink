#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
from PyQt4.QtGui import QShortcut
import QTermWidget
from QTermWidget import QTermWidget
from cink import Center

class deneme(QTermWidget,Center):
    def __init__(self,parent=None):
        QTermWidget.__init__(self)
        self.center(self)
        

def main():

    a=Qt.QApplication(sys.argv)
    w=QTermWidget.QTermWidget()
    w.show()

    return a.exec_()

if __name__=="__main__":
    main()
