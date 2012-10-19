import gtk 
import vte

win = gtk.Window()
notebook = gtk.Notebook()
class Console(vte.Terminal,gtk.Notebook):

	def __init__(self):	 	
		terminal = vte.Terminal()
	        self.is_fullscreen = False
		terminal.fork_command('bash')
		terminal.set_background_transparent(1)  # set_background_transparent boolean degerler aliyo
#		notebook = gtk.Notebook()
		page = []
		page.append(gtk.VBox())
		win.reparent(page[0])
		notebook.set_tab_pos (gtk.POS_BOTTOM);  # sekme isimlerinin altta cikmasi icin
#		win.set_parent(page[0])
		#win.get_parent()  parent tab in ogrenilmesi icin
		page.append(gtk.VBox())

		page[0].add(terminal)
		page[1].add(terminal)
		notebook.append_page(page[0],gtk.Label('tab1'))	
		notebook.append_page(page[1], gtk.Label('tab2'))
#		notebook.set_tab_reorderable(page[0], True)   sekmelerin tasinabilmesi icin
#		notebook.set_tab_reorderable(page[1], True)				
		win.add(notebook) 
		#win.add(terminal)
		#vpaned = gtk.VPaned()   yatay bolme icin
		#win.add(vpaned)
		#vpaned.show()
		#vpaned.add1(terminal)
		#vpaned.add2(terminal)
	        win.connect('delete-event', lambda win, event: gtk.main_quit())
	        win.connect('key-press-event',self.full_screen)
	        terminal.connect('event',self.right_click)
                win.show_all()

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
			item2 = gtk.MenuItem("Paste")
			item3 = gtk.MenuItem("Close Tab")
			item4 = gtk.MenuItem("Quit")		
			item1.show()
			m.append(item1)
			item2.show()
                        m.append(item2)
			item3.show()
                        m.append(item3)
			item4.show()
                        m.append(item4)
           		m.popup(None, None, None, event.button, event.time, None)
 

if __name__ == '__main__':
	w = Console()
	gtk.main()

