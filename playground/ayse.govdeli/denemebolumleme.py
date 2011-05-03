#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import Qt
from  PyQt4.Qt import QMainWindow
from  PyQt4.Qt import QSplitter
import QTermWidget
from  PyQt4.Qt import QWidget

a = Qt.QApplication(sys.argv)
w = QTermWidget.QTermWidget()
w.setColorScheme(2)
w.setScrollBarPosition(2)
widget=QTermWidget.QTermWidget()
widget.setColorScheme(2)
widget.setScrollBarPosition(2)
form = Qt.QMainWindow()
form.resize(400,300)
w.resize(200,300)
widget.resize(200,300)
splitter = Qt.QSplitter(form)
splitter.resize(400,300)
splitter.setOrientation(Qt.Qt.Horizontal)
splitter.addWidget(widget)
splitter.addWidget(w)
w.setAutoFillBackground(True)
x=splitter.height()
y=splitter.width()
print 'x.',x
print 'y',y
form.show()
a.exec_()


