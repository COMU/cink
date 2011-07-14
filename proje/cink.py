#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore
from PyQt4 import Qt
import QTermWidget
from  PyQt4.Qt import QSplitter
from  PyQt4.Qt import QMainWindow
from PyQt4.QtGui import *
#from QTermWidget import QTermWidget

def sari():
    w.setColorScheme(3)
def gri():
    w.setColorScheme(1)
def yesil():
    w.setColorScheme(2)

#w.setColorScheme(SARI)

class Cink(Qt.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self) #QMainWindow tanımlanıyor.
        self.resize(640,320) #QMainWindow'un başlangıç büyüklüğü belirleniyor.
        self.splitter = Qt.QSplitter(self)
        self.setCentralWidget(self.splitter) #Yaratılan spliter mainwindowun üstüne yerleştiriliyor.
        self.splitter.addWidget(self.createWidget())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #QMainWindow'un üstündeki menubar kaldırılıyor.
        self.tabBar=QtGui.QTabBar(self)
        self.tabBar.addTab("Kabuk1")
        self.center() #mainwindow ortalanıyor.

    def newTab(self):
        self.tabBar.addTab("Kabuk")
        self.center()
#Terminal widget oluşturuluyor

    def createWidget(self):
        widget=QTermWidget.QTermWidget() #widget nesnesi üretiliyor.
        widget.setColorScheme(2) #widgetin rengi belirleniyor.
        widget.setScrollBarPosition(2) #widgetin scroolbarın yeri belirleniyor.
        widget.setWindowFlags(QtCore.Qt.FramelessWindowHint) #menubar kaldırılıyor.
        return widget
#Dikey olarak bölümlendirme yapılıyor


    def Vertical(self): #dikey olarak bölme fonksiyonu
        #splitter = Qt.QSplitter(self)
        #splitter.setAutoFillBackground(True)
        newWidget=self.createWidget()
        self.splitter.setOrientation(Qt.Qt.Vertical)
        self.splitter.addWidget(newWidget)
        newWidget.setAutoFillBackground(True)


#Yatay olarak bölümlendirme yapılıyor


    def Horizontal(self): #yatay olarak bölme fonksiyonu
        #splitter = Qt.QSplitter(self)
        #splitter.setAutoFillBackground(True)
        newWidget=self.createWidget()
        self.splitter.setOrientation(Qt.Qt.Horizontal)
        self.splitter.addWidget(newWidget)
        newWidget.setAutoFillBackground(True)

    def yokedici(self):
        secilenWidget=self.focusWidget().parent()
        secilenSplitter=secilenWidget.parent()
        secilenWidget.hide()
        secilenSplitter.hide()

    def ekran(self): #tam ekran yapma fonksiyonu
        if(w.isFullScreen()==False):
            w.showFullScreen()

        else:
            w.showNormal()



    def center(self): #mainwindowun ortalanması
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        cntr=(screen.width()-size.width())/2
        self.setGeometry(cntr,0,size.width(),size.height())
        self.tabBar.setGeometry(0,self.height()-25,200*self.tabBar.count()-100,100)
#pencere boyutlarının ayarlanması----------------------------

    def artir(self): #pencerenin yanlara doğrultusunda büyütülmesi
        mesafe=QtGui.QDesktopWidget().screenGeometry().width()-w.width()
        while(True):
            screen = QtGui.QDesktopWidget().screenGeometry()
            en=w.width()
            boy=w.height()
            uzaklik=screen.width()- w.width()
            if(uzaklik>0):
                uzaklik=uzaklik-200
                if(uzaklik>200):
                    yeniuzaklik=screen.width()-uzaklik
                    w.resize(yeniuzaklik,boy)
                    w.center()
                    break
                else:
                    yeniuzaklik=screen.width()
                    w.resize(yeniuzaklik,boy)
                    w.center()
                    break
                break
            else:
                break

    def azalt(self): #pencerenin yanlara doğru küçültülmesi
        while(True):
            screen = QtGui.QDesktopWidget().screenGeometry()
            en=w.width()
            boy=w.height()
            uzaklik=screen.width()-w.width()
            if(uzaklik==0):
                uzaklik=uzaklik+200
                yeniuzaklik=screen.width()-uzaklik
                w.resize(yeniuzaklik,boy)
                w.center()
                break
            else:
                uzaklik=uzaklik+200
                yeniuzaklik=screen.width()-uzaklik
                if(yeniuzaklik>100):
                    w.resize(yeniuzaklik,boy)
                    w.center()
                    break
                else:
                    break
            break



    def boy_artir(self): #pencerenin yukarı-aşağı doğrultusunda büyütülmesi
        en=w.width()
        boy=w.height()
        while(True):
            screen = QtGui.QDesktopWidget().screenGeometry()
            if(boy<screen.height()):
                boy=boy+200
                if(boy<screen.height()):
                    w.resize(en,boy-25)
                    w.center()
                    break
                else:
                    w.resize(en,screen.height()-25)
                    break


    def boy_azalt(self): #pencerenin yukarı-aşağı doğrultusunda küçültülmesi
        while(True):
            screen = QtGui.QDesktopWidget().screenGeometry()
            en=w.width()
            boy=w.height()
            if(boy<(screen.height())):
                boy=boy-200
                if(boy>100):
                    w.resize(en,boy)
                    break
                else:
                    break
            else:
                break


#şeffaflığın ayarlanması-------------------------------------------

    def transparent_artma(self): #şeffaflığın artması
        w.setWindowOpacity(0.6)


    def transparent_azl(self): #şeffaflığın azaltılması
        w.setWindowOpacity(1.0)

#------------------------------------------------------------
    def keyPressEvent(self, event): #klavyeden tuşların girilmesi
        if type(event) == QtGui.QKeyEvent:
            #here accept the event and do something
            if (event.key()) == 16777264:
                print "aaa"
            print event.key()
            event.accept()
        else:
            event.ignore()

#QTermWidgeti import ettiğimizde keyPressEvent fonksiyonunu tekrar yazdığımızda daha önceki tanımlanmış olan kabul edilip işleniyor. O yüzden bu kısmı QTermWidgetin kaynak kodlarının içine eklemeyi düşünüyoruz.

#--------------------------------------------------------------

if __name__=='__main__':
    app=Qt.QApplication(sys.argv)
    w = Cink()
    w.show()
    kisayol6=QShortcut("Ctrl+F11",w,w.ekran)
    art=QShortcut("ALT+k",w,w.artir)
    azalt=QShortcut("ALT+m",w,w.azalt)
    boy_art=QShortcut("ALT+j",w,w.boy_artir)
    boy_azalt=QShortcut("ALT+n",w,w.boy_azalt)
    kapat=QShortcut("ALT+c",w,w.close)
    kisayol1=QShortcut("Alt+g",w,gri)
    kisayol2=QShortcut("ALT+y",w,yesil)
    kisayol3=QShortcut("ALT+s",w,sari)
    transparent_art=QShortcut("Ctrl+e",w,w.transparent_artma)
    transparent_azl=QShortcut("Ctrl+w",w,w.transparent_azl)
    shortcut = QShortcut("Ctrl+a",w,w.Horizontal)
    shortcut = QShortcut("Ctrl+g",w,w.Vertical)
    shortcut = QShortcut("Shift+Ctrl+n",w,w.newTab)
    shortcut = QShortcut("Ctrl+d",w,w.yokedici)
    #form.show()
    app.exec_()

