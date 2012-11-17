import os
import gtk
import vte

class Utils():

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
                quit_item = gtk.MenuItem("Quit")
                quit_item.connect("activate", lambda discard: gtk.main_quit())  
                quit_item.show()
                m.append(quit_item)
                m.popup(None, None, None, event.button, event.time, None)

    def copy(self, widget=None, data=None):
        if self.terminal[self.index_].get_has_selection():
            self.terminal[self.index_].copy_clipboard()

    def paste(self, widget=None, data=None):
        self.terminal[self.index_].paste_clipboard()

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
            del self.terminal[pagenum]
            self.notebook.remove_page(pagenum)

    def tab_rename(self,widget=None,data=None):
        pagenum = self.notebook.get_current_page()
        self.entry = gtk.Entry()
        self.hbox[pagenum].remove(self.label[pagenum])        
        self.entry.set_text(self.label[pagenum].get_text())
        self.hbox[pagenum].pack_start(self.entry)       
        self.hbox[pagenum].show_all()
        self.entry.connect('key-press-event', self.enter_key)   
    
    def enter_key(self, widget, event):
        pagenum = self.notebook.get_current_page()
        self.str_ = self.entry.get_text()
        if event.keyval == 65293:
            # kullanici string girmwzse eski adi alir
            if self.str_ == "":
                self.label[pagenum].set_text(self.label[pagenum].get_text())

            else:
                self.label[pagenum].set_text(self.str_)
            self.hbox[pagenum].remove(self.entry)
            self.hbox[pagenum].pack_start(self.label[pagenum])
            self.hbox[pagenum].show_all()

    def tab_name_no(self):
        if len(self.label)==0:
            print "tek eleman var"
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


