import os
import gtk
import vte

class Utils():

    def start_term(self,accelgroup,win,key,mod):
	print "**"
	
    def create_tab_(self,accelgroup,win,key,mod):
        self.create_tab()
    
    def close_tab_(self,accelgroup,win,key,mod):
        self.close_tab()

    def right_click(self,widget,event):
        if event.type == gtk.gdk.BUTTON_PRESS:
            if event.button == 3:    # 1 sol tus,2 orta tus icin
                m = gtk.Menu()
                copy_item = gtk.MenuItem("Copy")
                copy_item.show()
                m.append(copy_item)
                copy_item.connect("activate",self.copy)
                paste_item = gtk.MenuItem("Paste")
                paste_item.show()
                m.append(paste_item)
                paste_item.connect("activate",self.paste)
                close_tab_item = gtk.MenuItem("Close Tab")
                close_tab_item.show()
                m.append(close_tab_item)
                close_tab_item.connect("activate",self.close_tab)
                new_tab_item = gtk.MenuItem("New Tab")  
                new_tab_item.show()
                m.append(new_tab_item)
                new_tab_item.connect("activate",self.create_tab)
                rename_item = gtk.MenuItem("Tab Rename")
                rename_item.show()
                rename_item.connect("activate",self.tab_rename) 
         	m.append(rename_item)
		pref_item=gtk.MenuItem("Preferences")
		pref_item.show()
		pref_item.connect("activate",self.pref_tab)
		m.append(pref_item)
                quit_item = gtk.MenuItem("Quit")
                quit_item.connect("activate", lambda discard: gtk.main_quit())  
                quit_item.show()
                m.append(quit_item)
                m.popup(None, None, None, event.button, event.time, None)

    def copy(self, widget=None, data=None):
        if self.vteObj.terminal[self.vteObj.index_].get_has_selection():
            self.vteObj.terminal[self.vteObj.index_].copy_clipboard()

    def paste(self, widget=None, data=None):
        self.vteObj.terminal[self.vteObj.index_].paste_clipboard()

    def close_tab(self,widget=None,data=None):
        # o anki sayfanin numarasinin alinmasi
        # her sayfa kapatildiginda toplam sekme sayisi bir azaltilir bu sekilde
        self.page_ -=1
        pagenum = self.notebook.get_current_page()
        #acik tek bir sekme kaldiysa ve kapatiliyorsa pencerenin de kapatilmasi
        if self.page_ == 0:
            gtk.main_quit()
        # degilse sadece tabin kapatilmasi icin
        else:
            del self.hbox[pagenum]
            del self.label[pagenum]
            del self.vteObj.terminal[pagenum]
            self.notebook.remove_page(pagenum)

    def tab_rename(self,widget=None,data=None):
        pagenum = self.notebook.get_current_page()
        self.entry = gtk.Entry()
	self.entry.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("gray"))
	self.entry.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("blue"))
	self.entry.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
	self.entry.set_width_chars(len(self.label[pagenum].get_text()))
        self.hbox[pagenum].remove(self.label[pagenum])        
        self.entry.set_text(self.label[pagenum].get_text())
	self.entry.select_region(0, len(self.entry.get_text()))
        self.hbox[pagenum].pack_start(self.entry)       
        self.hbox[pagenum].show_all()
        self.entry.connect('key-press-event', self.enter_key)   
    
    def enter_key(self, widget, event):
        pagenum = self.notebook.get_current_page()
        self.str_ = self.entry.get_text()
        if event.keyval == 65293:
            # kullanici string girmezse eski adi alir
            if self.str_ == "":
                self.label[pagenum].set_text(self.label[pagenum].get_text())

            else:
                self.label[pagenum].set_text(self.str_)
            self.hbox[pagenum].remove(self.entry)
            self.hbox[pagenum].pack_start(self.label[pagenum])
            self.hbox[pagenum].show_all()

    def tab_name_no(self):
        if len(self.label)==0:
            self.label.append(gtk.Label("tab1"))
            return
        tab_name = ""
        self.name_list = []
	#tum isimleri kontrol icin bir listeye gonderir
        for j in range(0,len(self.label)):
            self.name_list.append(self.label[j].get_text())
        for i in range(0,len(self.label)):
            name = tab_name.join("tab"+str(i+1))
            if not name in self.name_list:
                self.label.append(gtk.Label(name))
                return
        self.label.append(gtk.Label("tab"+str(i+2)))
        return

    def pref_tab(self,widget=None,data=None):
    	o = ColorSelection_()
	o.color_tab()

class ColorSelection_:
	def __init__(self):
        	self.w = gtk.Window()
		self.w.set_title("Tercihler")
	        self.w.set_size_request(600, 400)
        	self.notebook = gtk.Notebook()
	        self.w.add(self.notebook)
	def color_tab(self):
		hbox1 = gtk.HBox(False, 0)
		hbox2 = gtk.HBox(False,0)
		hbox3 = gtk.HBox(False,0)
	        label1 = gtk.Label("Yazi Rengi Secimi")
		label2 = gtk.Label("Terminal Rengi Secimi")
		label3 = gtk.Label("Yazi Buyuklugu")
		c1 = gtk.ColorSelection()
		c1.connect('color-changed', self.text_color)
		c2 = gtk.ColorSelection()	
		c2.connect('color-changed', self.term_color)
        	hbox1.pack_start(label1)
		hbox2.pack_start(label2)
#		hbox.pack_start(label3)
		self.notebook.insert_page(c1, hbox1)
		self.notebook.insert_page(c2,hbox2)
		hbox1.show_all()
		hbox2.show_all()
		self.w.show_all()
	def text_color(*args):
		color=c.get_current_color()
		
	def term_color(*args):
		color=c.get_current_color()

