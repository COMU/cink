#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore
from PyQt4 import Qt
from PyQt4.QtGui import QShortcut
from QTermWidget import QTermWidget


class Center(QTermWidget):
    def __init__(self,parent=None):
        QTermWidget.__init__(self)
        self.center()


    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        cntr=(screen.width()-size.width())/2
  #      self.move((screen.width()-size.width())/2, 0)
        self.setGeometry(cntr,25,size.width(),size.height())



def artir():
    mesafe=QtGui.QDesktopWidget().screenGeometry().width()-w.width()
    while(True):
        screen = QtGui.QDesktopWidget().screenGeometry()
        en=w.width()
        boy=w.height()
        uzaklik=screen.width()- w.width()
        if(uzaklik>=10):
            uzaklik=screen.width()- w.width()
            uzaklik=uzaklik-(uzaklik/5)
            yeniuzaklik=screen.width()-uzaklik
            w.resize(yeniuzaklik,boy)
            w.center()
            break
        else:
            break

def azalt():
    while(True):
        screen = QtGui.QDesktopWidget().screenGeometry()
        en=w.width() 
        boy=w.height()
        uzaklik=screen.width()-w.width()
        if(uzaklik>=0):
            if(en>(uzaklik/5)):
                uzaklik=uzaklik+(uzaklik/5)
                yeniuzaklik=screen.width()-uzaklik
                w.resize(yeniuzaklik,boy)
                w.center()
                break
            break
        else:
            break

def boy_artir():
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

        

def boy_azalt():
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

def gorunme():
    while(True):
        a=0
        w.setGeometry(0,-(w.height()+20),w.width(),w.height())
        break
        



def ekran():
    if(w.isFullScreen()==False):
        w.showFullScreen()
    else:
        w.showNormal()

if __name__=='__main__':
    app=Qt.QApplication(sys.argv)
    w = Center()
    w.setScrollBarPosition(2)
    w.show()
    kisayol6=QShortcut("Ctrl+F11",w,ekran)
    art=QShortcut("ALT+k",w,artir)
    azalt=QShortcut("ALT+m",w,azalt)
    boy_art=QShortcut("ALT+j",w,boy_artir)
    boy_azalt=QShortcut("ALT+n",w,boy_azalt)
    gorun=QShortcut("a",w,gorunme)
    app.exec_()



