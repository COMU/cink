import gtk 
import vte
import os

win = gtk.Window()
class Console(vte.Terminal,gtk.Window):


	def __init__(self):	 	
        
		self.terminal = vte.Terminal()
	        self.is_fullscreen = False
		argv = ['bash']
		env = self.env_map_to_list(os.environ.copy())
		cwd = os.environ['HOME']  # eger os.getcwd() deseydik o an calistigi yerin yolunu geri dondururdu
		self.terminal.fork_command(argv[0], argv, env, cwd)
		win.resize(100,30)
		self.terminal.set_background_transparent(1)  # set_background_transparent boolean degerler aliyo
	        win.connect('delete-event', lambda win, event: gtk.main_quit())
		win.connect('key-press-event',self.full_screen)
	        self.terminal.connect('event',self.right_click)
		win.add(self.terminal)
                win.show_all()

	def env_map_to_list(self, env): # terminal fork_command icin
		return ['%s=%s' % (k, v) for (k, v) in env.items()]
	def pageSelected(self, notebook, page, pagenum):
		name = notebook.get_tab_label(notebook.get_nth_page(pagenum))
		if name == 'tab1':	
			print "-"
			print notebook.get_nth_page(pagenum)
		

	def full_screen(self, widget, event):
		 if  event.keyval == gtk.keysyms.F11:
			if self.is_fullscreen == False:
                                win.fullscreen()
                                self.is_fullscreen = True
                        elif self.is_fullscreen == True:
                                win.unfullscreen()
                                self.is_fullscreen = False
	def right_click(self,widget,event):
		if event.type == gtk.gdk.BUTTON_PRESS:
	            if event.button == 3:    # 1 sol tus,2 orta tus icin
			m = gtk.Menu()
			item1 = gtk.MenuItem("Copy")
			item1.connect("activate",self.copy)
			item2 = gtk.MenuItem("Paste")
			item2.connect("activate",self.paste)
			item3 = gtk.MenuItem("Close Tab")
			item4 = gtk.MenuItem("Quit")	
			item4.connect("activate", lambda discard: gtk.main_quit())
			item1.show()
			m.append(item1)
			item2.show()
                        m.append(item2)
			item3.show()
                        m.append(item3)
			item4.show()
                        m.append(item4)
           		m.popup(None, None, None, event.button, event.time, None)
		
	def copy(self, widget=None, data=None):
		if self.terminal.get_has_selection():
			self.terminal.copy_clipboard()
	def paste(self, widget=None, data=None):
		self.terminal.paste_clipboard()

if __name__ == '__main__':
	w = Console()
	gtk.main()

