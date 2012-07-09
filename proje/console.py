#!/usr/bin/env python

from gi.repository import GLib
import gtk
import vte
import os

class Console():

	def __init__(self):
		terminal = vte.Terminal()
		terminal.fork_command('bash')
		win = gtk.Window()
		win.set_resizable(False)
		win.connect('delete-event', gtk.main_quit)
		win.set_opacity(0.8) #konsolu seffaf goruntuleme
		win.move(300,0) #konsolun konumu
		win.add(terminal)
		win.show_all()

	def console_bol(self):
		win.add(terminal)

if __name__=='__main__':
	Console()
	gtk.main()
