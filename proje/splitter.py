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
        #self.splitter.resize(640,320)
        self.setAutoFillBackground(True)
        self.splitter.setOpaqueResize(True)
        #self.splitter.resize(640,320)
        self.setCentralWidget(self.splitter) #Yaratılan splitter mainwindowun üstüne yerleştiriliyor.
        self.firstWidget=self.createWidget()
        self.firstWidget.setParent(self.splitter)
        #self.splitter.addWidget(self.createWidget())
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #QMainWindow'un üstündeki menubar kaldırılıyor.
        self.center() #mainwindow ortalanıyor.


    def createWidget(self):
        widget=QTermWidget.QTermWidget() #widget nesnesi üretiliyor.
        widget.setColorScheme(2) #widgetin rengi belirleniyor.
        widget.setScrollBarPosition(2) #widgetin scroolbarın yeri belirleniyor.
        widget.setWindowFlags(QtCore.Qt.FramelessWindowHint) #menubar kaldırılıyor.
        return widget

    def Vertical(self): #dikey olarak bölme fonksiyonu
        selectedWidget=self.focusWidget().parent()
        selectedSplitter=selectedWidget.parent()
        selectedWidget.hide()
        newWidget=self.createWidget()
        selectedSplitter.setOrientation(Qt.Qt.Vertical)
        splitter1=Qt.QSplitter(selectedSplitter)
        splitter2=Qt.QSplitter(selectedSplitter)
        splitter1.setAutoFillBackground(True)
        splitter2.setAutoFillBackground(True)
        selectedWidget.setParent(splitter1)
        newWidget.setParent(splitter2)
        newWidget.setFocus()
        selectedWidget.show()
        newWidget.show()

    def Horizontal(self): #yatay olarak bölme fonksiyonu
        selectedWidget=self.focusWidget().parent()
        selectedSplitter=selectedWidget.parent()
        selectedWidget.hide()
        newWidget=self.createWidget()
        selectedSplitter.setOrientation(Qt.Qt.Horizontal)
        selectedSplitter.setOpaqueResize(True)
        splitter1=Qt.QSplitter(self.splitter)
        splitter2=Qt.QSplitter(self.splitter)
        selectedWidget.setParent(splitter1)
        newWidget.setParent(splitter2)
        newWidget.setFocus()
        selectedWidget.show()
        newWidget.show()


    def center(self): #mainwindowun ortalanması
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        cntr=(screen.width()-size.width())/2
        self.setGeometry(cntr,0,size.width(),size.height())
        #self.tabBar.setGeometry(0,self.height()-25,200*self.tabBar.count()-100,100)

if __name__=='__main__':
    app=Qt.QApplication(sys.argv)
    w = Cink()
    w.show()
    shortcut = QShortcut("Ctrl+a",w,w.Horizontal)
    shortcut = QShortcut("Ctrl+g",w,w.Vertical)
    app.exec_()





