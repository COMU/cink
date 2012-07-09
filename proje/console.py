#!/usr/bin/env python

from gi.repository import GLib
import gtk
import vte
import os

win=gtk.Window()
class Console(vte.Terminal):

	def __init__(self, *args, **kwds):
		terminal = vte.Terminal()
		terminal.fork_command('bash')
		win.set_resizable(False)
		win.connect('delete-event', gtk.main_quit)
		win.connect("key_press_event", self.key_pressed)
		win.move(300,0) #konsolun konumu
		win.add(terminal)
		win.show_all()

	def key_pressed(self,widget,event):
    		if event.keyval == gtk.gdk.keyval_from_name('space') and event.state & gtk.gdk.CONTROL_MASK:
      			return self.seffaflik_kaldir()
		if event.keyval == gtk.gdk.keyval_from_name('F11') :
			return self.seffaf()
    		return False	

	def tamekran(self):
		win.fullscreen()

	def console_bol(self):
		win.add(terminal)

	def seffaflik_kaldir(self):
		win.set_opacity(1.0)	

	def seffaf(self):
		win.set_opacity(0.8)
	
if __name__=='__main__':
	w = Console()
	gtk.main()
