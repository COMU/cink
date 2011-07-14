#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore
from PyQt4 import Qt
import QTermWidget
from  PyQt4.Qt import QSplitter
from  PyQt4.Qt import QMainWindow
from PyQt4.QtGui import *



class Cink(Qt.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self) #QMainWindow tanımlanıyor.
        self.resize(640,320) #QMainWindow'un başlangıç büyüklüğü belirleniyor.
        self.splitter = Qt.QSplitter(self)
        self.setAutoFillBackground(True)
        self.splitter.setOpaqueResize(True)
        self.setCentralWidget(self.splitter) #Yaratılan splitter mainwindowun üstüne yerleştiriliyor.
        self.firstWidget=self.createWidget()
        print"ilk",self.firstWidget
        print "splitter",self.splitter
        self.firstWidget.setParent(self.splitter)
        #self.splitter.addWidget(self.createWidget())
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #QMainWindow'un üstündeki menubar kaldırılıyor.


    def createWidget(self):
        widget=QTermWidget.QTermWidget() #widget nesnesi üretiliyor.
        widget.setColorScheme(2) #widgetin rengi belirleniyor.
        widget.setScrollBarPosition(2) #widgetin scroolbarın yeri belirleniyor.
        widget.setWindowFlags(QtCore.Qt.FramelessWindowHint) #menubar kaldırılıyor.
        return widget

    def Vertical(self): #dikey olarak bölme fonksiyonu
        selectedWidget=w.focusWidget().parent()
        selectedSplitter=selectedWidget.parent()
        selectedWidget.hide()
        newWidget=self.createWidget()
        splitter1=Qt.QSplitter(selectedSplitter)
        selectedWidget.setParent(splitter1)
        splitter2=Qt.QSplitter(selectedSplitter)
        newWidget.setParent(splitter2)
        selectedSplitter.setOrientation(Qt.Qt.Vertical)
        selectedWidget.show()
        newWidget.show()
        newWidget.setFocus()


    def Horizontal(self): #yatay olarak bölme fonksiyonu
        selectedWidget=w.focusWidget().parent()
        selectedSplitter=selectedWidget.parent()
        selectedWidget.hide()
        newWidget=self.createWidget()
        selectedSplitter.setOrientation(Qt.Qt.Horizontal)
        splitter1=Qt.QSplitter(selectedSplitter)
        selectedWidget.setParent(splitter1)
        splitter2=Qt.QSplitter(selectedSplitter)
        newWidget.setParent(splitter2)
        selectedWidget.show()
        newWidget.show()
        newWidget.setFocus()

if __name__=='__main__':
    app=Qt.QApplication(sys.argv)
    w = Cink()
    w.show()
    shortcut = QShortcut("Ctrl+Shift+a",w,w.Horizontal)
    shortcut = QShortcut("Ctrl+Shift+g",w,w.Vertical)
    app.exec_()






