import gtk 
import vte
import os

win = gtk.Window()
class Console(vte.Terminal):


	def __init__(self):	 	
        	self.page_ = 1
		win.resize(400,400)
	        win.connect('delete-event', lambda win, event: gtk.main_quit())
		win.connect('key-press-event',self.full_screen)
		self.notebook = gtk.Notebook()
		win.add(self.notebook)	
		self.notebook.set_tab_pos(gtk.POS_BOTTOM)
		self.create_tab(widget=None,data=None) # sag tiklamayla aktif olsun diye uc tane arg verildi

	def create_terminal(self):
		self.argv = ['bash']
		self.env = self.env_map_to_list(os.environ.copy())
		self.cwd = os.environ['HOME']
		self.is_fullscreen = False
		self.terminal = vte.Terminal()
#		self.terminal.set_background_transparent(1)

	def terminal_action(self):
		self.create_terminal()
                self.terminal.fork_command(self.argv[0], self.argv, self.env, self.cwd)
		self.terminal.connect('event',self.right_click)

	def create_tab(self,widget=None,data=None):
		self.page_ = self.page_+1
		for i in range(1,2):
                        hbox = gtk.HBox(False, 0)
			hbox.set_spacing(1)
                        label = gtk.Label("tab"+str(self.page_-1))
                        hbox.pack_start(label)
			# sekmelerde kapatma simgesinin gelmesi icin
			close_image = gtk.image_new_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
		        image_w, image_h = gtk.icon_size_lookup(gtk.ICON_SIZE_MENU)
			# sekmenin uzerinde sekme kapatma ozelligi olmasi icin 
			btn = gtk.Button()
		        btn.set_relief(gtk.RELIEF_NONE)
		        btn.set_focus_on_click(False)
		        btn.add(close_image)
		        hbox.pack_start(btn, False, False)
			# kapatma butonunun boyutunun ayarlanmasi icin			
			style = gtk.RcStyle()
		        style.xthickness = 0
		        style.ythickness = 0
		        btn.modify_style(style)			

			hbox.show_all()
			# sekmenin terminal olusturulmasi
			self.terminal_action()
			# yeni sekme acilmasi
                        self.notebook.insert_page(self.terminal,hbox)
			# sekme kapatmak icin fonksiyonun aktif edilmesi
			btn.connect('clicked', self.on_closetab_button_clicked, self.terminal)
			win.show_all() # yeni sekme istendiginde bulunuldugunda window kendini guncellesin diye buraya yazildi
			self.notebook.set_current_page(self.page_-2)  # yeni sekme acildiginda direkt o sekmeye gecsin diye eklendi

	def on_closetab_button_clicked(self, sender, widget):
	        # o anki sayfanin numarasinin alinmasi
		self.page_ = self.page_-1 # her sayfa kapatildiginda toplam sekme sayisi bir azaltilir bu sekilde
        	pagenum = self.notebook.page_num(widget)
		if self.page_ == 1: #acik tek bir sekme kaldiysa ve kapatiliyorsa pencerenin de kapatilmasi icin
			gtk.main_quit()
		else:
	        	self.notebook.remove_page(pagenum)

 	def env_map_to_list(self, env): # terminal fork_command icin
		return ['%s=%s' % (k, v) for (k, v) in env.items()]

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
			item4 = gtk.MenuItem("New Tab")	
			item5 = gtk.MenuItem("Quit")
			item4.connect("activate",self.create_tab)
			item5.connect("activate", lambda discard: gtk.main_quit())
			item1.show()
			m.append(item1)
			item2.show()
                        m.append(item2)
			item3.show()
                        m.append(item3)
			item4.show()
                        m.append(item4)	
                        item5.show()
			m.append(item5)
           		m.popup(None, None, None, event.button, event.time, None)
		
	def copy(self, widget=None, data=None):
		if self.terminal.get_has_selection():
			self.terminal.copy_clipboard()

	def paste(self, widget=None, data=None):
		self.terminal.paste_clipboard()

if __name__ == '__main__':
	w = Console()
	gtk.main()

