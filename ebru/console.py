import gtk 
import vte

win = gtk.Window()
class Console(vte.Terminal):

	def __init__(self):
	 	
		terminal = vte.Terminal()
		terminal.fork_command('bash')
		terminal.connect('event',self.right_click)
		terminal.set_background_transparent(1)  # set_background_transparent boolean degerler aliyo
	        win.add(terminal)
		win.connect('key-press-event',self.full_screen)
		self.is_fullscreen = False
	        win.connect('delete-event', lambda win, event: gtk.main_quit())
                win.show_all()
#		gtk.Window(type=gtk.WINDOW_TOPLEVEL)
	def full_screen(self, widget, event):
		 if  event.keyval == gtk.keysyms.F11:
			if self.is_fullscreen == False:
                                win.fullscreen()
                                self.is_fullscreen = True
                        elif self.is_fullscreen == True:
                                win.unfullscreen()
                                self.is_fullscreen = False

	
	def right_click(self,terminal,event):
		if event.type == gtk.gdk.BUTTON_PRESS:
	            if event.button == 3:    # 1 sol tus,2 orta tus icin
        	        print "sag tusa basildi."


if __name__ == '__main__':
	w = Console()
	gtk.main()

