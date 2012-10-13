import gtk
import vte

class Console:
	
	def __init__(self):
	 	
		terminal = vte.Terminal()
		terminal.fork_command('bash')
		terminal.connect('event',self.right_click)
		win = gtk.Window()
		terminal.set_background_transparent(1)
	        win.add(terminal)
		win.connect('key-press-event',self.shortcut)
	        win.connect('delete-event', lambda win, event: gtk.main_quit())
	        win.show_all()	

	def shortcut(self, widget, event, *args):
                if event.keyval == gtk.keysyms.F6:
                        print "F6 ya basildi"


	def right_click(self,terminal,event):
		if event.type == gtk.gdk.BUTTON_PRESS:
	            if event.button != 3:
        	        return
	            else:
	                print "right button pressed"


if __name__ == '__main__':
	w = Console()
	gtk.main()

