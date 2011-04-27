#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QShortcut
import QTermWidget
from PyQt4 import QtCore
from PyQt4 import Qt
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPixmap
from PyQt4.Qt import *

def kapatma():
    app.exit()

def transparent():
    widget.setWindowOpacity(0.6)


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    widget = QTermWidget.QTermWidget()
    #widget.setStyleSheet("background-color: rgba(255, 255, 255, 0%);")
    #widget.setWindowOpacity(0.5)
    #widget.setBackgroundRole(QtGui.QPalette.Base)
    #widget.setAttribute(Qt.WA_NoSystemBackground, True)
    #widget.setAttribute(Qt.WA_TranslucentBackground)
    widget.resize(500, 500)
    widget.setWindowTitle('konsol')
    shortcut1=QShortcut("Ctrl+c",widget,kapatma)
    shortcut2=QShortcut("@",widget,transparent)
    widget.setScrollBarPosition(2)
    widget.setColorScheme(2)

    widget.show()
    sys.exit(app.exec_())

