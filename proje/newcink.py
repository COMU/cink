#ifndef NEWWIDGET.PY
#define NEWWIDGET.PY
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import Qt
import QTermWidget
from PyQt4.QtGui import QShortcut
from PyQt4 import QtGui,QtCore
from  PyQt4.Qt import QMainWindow
from  PyQt4.Qt import QSplitter

a = Qt.QApplication(sys.argv)
w = QTermWidget.QTermWidget()
w.setColorScheme(2)
w.setScrollBarPosition(2)
w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
form = Qt.QMainWindow()
form.resize(w.width(),w.height())
form.autoFillBackground()
splitter = Qt.QSplitter(form)
splitter.resize(w.width(),w.height())
splitter.setAutoFillBackground(True)
splitter.addWidget(w)
w.setAutoFillBackground(True)
#form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
screen = QtGui.QDesktopWidget().screenGeometry()
size =  form.geometry()
cntr=(screen.width()-size.width())/2
form.setGeometry(cntr,0,size.width(),size.height())

def createWidget():
    widget=QTermWidget.QTermWidget()
    widget.setColorScheme(2)
    widget.setScrollBarPosition(2)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    return widget

def setHorizontal():
    newWidget=createWidget()
    splitter.setOrientation(Qt.Qt.Horizontal)
    splitter.addWidget(newWidget)
    newWidget.setAutoFillBackground(True)


def setVertical():
    newWidget=createWidget()
    splitter.setOrientation(Qt.Qt.Vertical)
    splitter.addWidget(newWidget)
    newWidget.setAutoFillBackground(True)

shortcut = QShortcut("Ctrl+a",form,setHorizontal)
shortcut = QShortcut("Ctrl+g",form,setVertical)

form.show()
a.exec_()
