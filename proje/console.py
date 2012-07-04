#!/usr/bin/env python

from gi.repository import Gtk, Vte
from gi.repository import GLib
import os
class Console():
	def __init__(self):
		terminal = Vte.Terminal()
		terminal.fork_command_full(Vte.PtyFlags.DEFAULT, os.environ['HOME'], ["/bin/bash"], [], GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None,)
		win = Gtk.Window()
		win.connect('delete-event', Gtk.main_quit)
		win.set_position(Gtk.WindowPosition.CENTER)
		win.add(terminal)
		win.show_all()

	def console_bol(self):
		win.add(terminal)

if __name__=='__main__':
	Console()
	Gtk.main()
