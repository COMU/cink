#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore
from PyQt4 import Qt
from PyQt4.QtGui import QShortcut
from QTermWidget import QTermWidget


def sari():
    w.setColorScheme(3)
def gri():
    w.setColorScheme(1)
def yesil():
    w.setColorScheme(2)
#def tamekran():
  #  w.resize(2048,2048)
#def tam_ekranlScreen()
#def normal_ekran():
  #  w.showNormal()
#aynı tuşu kullanarak konsolu büyütüp küçültme
"""def ekran():
    if(w.isFullScreen()==False):
        w.showFullScreen()
    else:
        w.showNormal()"""
#konsolun boyutlarının değiştirilmesi


class Cink(QTermWidget):
    def __init__(self,parent=None):
        QTermWidget.__init__(self)
        self.center()
    
    def ekran(self):
        if(w.isFullScreen()==False):
            w.showFullScreen()
        else:
            w.showNormal()    

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        cntr=(screen.width()-size.width())/2
  #      self.move((screen.width()-size.width())/2, 0)
        self.setGeometry(cntr,0,size.width(),size.height())

    def artir(self):
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

    def azalt(self):
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

    def boy_artir(self):
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


    def boy_azalt(self):
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

    def transparent_artma(self):
        w.setWindowOpacity(0.6)

    def transparent_azl(self):
        w.setWindowOpacity(1.0)

    def kapama(self):
        w.close()

if __name__=='__main__':
    a=Qt.QApplication(sys.argv)
    w = Cink()
    w.setScrollBarPosition(2)
    w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    w.setColorScheme(2)
    w.show()
    kisayol6=QShortcut("Ctrl+F11",w,w.ekran)
    art=QShortcut("ALT+k",w,w.artir)
    azalt=QShortcut("ALT+m",w,w.azalt)
    boy_art=QShortcut("ALT+j",w,w.boy_artir)
    boy_azalt=QShortcut("ALT+n",w,w.boy_azalt)
    kapat=QShortcut("ALT+c",w,w.kapama)
    kisayol1=QShortcut("Alt+g",w,gri)
    kisayol2=QShortcut("ALT+y",w,yesil)
    kisayol3=QShortcut("ALT+s",w,sari)
    transparent_art=QShortcut("Ctrl+q",w,w.transparent_artma)
    transparent_azl=QShortcut("Ctrl+w",w,w.transparent_azl)
    a.exec_()




# kisayol4=QShortcut("SHIFT+CTRL+F11",w,tamekran)
