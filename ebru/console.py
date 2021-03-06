import gtk 
import vte
import os


win = gtk.Window()
class Console():
    def __init__(self):
        self.page_ = 1
        self.label = []  
        self.hbox = []
        win.resize(400,400)
        win.connect('delete-event', lambda win, event: gtk.main_quit())
        self.notebook = gtk.Notebook()
        win.add(self.notebook)	
        self.notebook.set_tab_pos(gtk.POS_BOTTOM)
        self.shortcut()
        self.create_tab(widget=None,data=None) #sag tiklamayla aktif olsun diye uc tane arg verildi


    def shortcut(self):
        accelgroup = []
        accelgroup.append(gtk.AccelGroup())
        # full screen
        key1, mod1 = gtk.accelerator_parse("F11")
        accelgroup[0].connect_group(key1,mod1,gtk.ACCEL_MASK,self.full_screen)
        # new tab
        key2, mod2= gtk.accelerator_parse("<Control><Shift>N") 
        accelgroup.append(gtk.AccelGroup())
        accelgroup[1].connect_group(key2,mod2,gtk.ACCEL_MASK,self.create_tab_)
        # close tab
        accelgroup.append(gtk.AccelGroup())
        key3, mod3= gtk.accelerator_parse("<Control><Shift>W") 
        accelgroup[2].connect_group(key3,mod3,gtk.ACCEL_MASK,self.close_tab_)
        # add accel
        win.add_accel_group(accelgroup[0])
        win.add_accel_group(accelgroup[1])
        win.add_accel_group(accelgroup[2])
        

    def create_tab_(self,accelgroup,win,key,mod):
        self.create_tab()
    
    def close_tab_(self,accelgroup,win,key,mod):
        self.close_tab()

    def create_tab(self,widget=None,data=None):
        self.page_ = self.page_+1
        self.index_ = self.page_-2
        self.notebook.set_scrollable(True)
        self.hbox.append(gtk.HBox(False, 0))
        self.hbox[self.index_].set_spacing(1)
        self.label.append(gtk.Label("tab"+str(self.page_-1)))  # daha sonra label degerleri degsitirlebilsin diye diziye atildi
        self.hbox[self.index_].pack_start(self.label[self.index_])
            # sekmelerde kapatma simgesinin gelmesi icin
        close_image = gtk.Image()
        close_image.set_from_file("close_button.png")
        close_image.show()
            # sekmenin uzerinde sekme kapatma ozelligi olmasi icin 
        btn = gtk.Button()
        btn.set_size_request(30,30)
        btn.set_relief(gtk.RELIEF_NONE)
        btn.set_focus_on_click(False)
        btn.add(close_image)
        self.hbox[self.index_].pack_end(btn, False, False)
            # kapatma butonunun boyutunun ayarlanmasi icin
        style = gtk.RcStyle()
        style.xthickness = 0
        style.ythickness = 0
        btn.modify_style(style)
        self.hbox[self.index_].show_all()
        # terminalin bolunmesi
        vpane = gtk.VPaned()
        term1 = self.terminal_action()
        vpane.add1(term1)
        
        term2 = self.terminal_action()
        vpane.add2(term2)        
        self.notebook.insert_page(vpane,self.hbox[self.index_])
        
            # sekme kapatmak icin fonksiyonun aktif edilmesi
        btn.connect('clicked', self.close_tab)

        win.show_all() # yeni sekme istendiginde bulunuldugunda window kendini guncellesin diye buraya yazildi
        self.notebook.set_current_page(self.page_-2)  # yeni sekme acildiginda direkt o sekmeye gecsin diye eklendi

    def create_terminal(self):
        self.argv = ['bash']
        self.env = self.env_map_to_list(os.environ.copy())
        self.cwd = os.environ['HOME']
        self.is_fullscreen = False
        self.terminal = vte.Terminal()
        self.terminal.set_colors(gtk.gdk.color_parse('white'),gtk.gdk.color_parse('pink'),[])
#        self.terminal.set_background_transparent(1)

    def terminal_action(self):
        self.create_terminal()
        self.terminal.fork_command(self.argv[0], self.argv, self.env, self.cwd)
        self.terminal.connect('event',self.right_click)
        return self.terminal

    def close_tab(self,widget=None,data=None):
        # o anki sayfanin numarasinin alinmasi
        self.page_ = self.page_-1 # her sayfa kapatildiginda toplam sekme sayisi bir azaltilir bu sekilde
        pagenum = self.notebook.get_current_page()
        if self.page_ == 1: #acik tek bir sekme kaldiysa ve kapatiliyorsa pencerenin de kapatilmasi icin
            gtk.main_quit()
        else:
            self.notebook.remove_page(pagenum)

    def env_map_to_list(self, env): # terminal fork_command icin
        return ['%s=%s' % (k, v) for (k, v) in env.items()]

    def full_screen(self,accelgroup,win,key,mod):
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
                copy_item = gtk.MenuItem("Copy")
                copy_item.show()
                m.append(copy_item)
                copy_item.connect("activate",self.copy)
                paste_item = gtk.MenuItem("Paste")
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
                rename_item = gtk.MenuItem("Oturumu Yeniden Adlandir")
                rename_item.show()
                rename_item.connect("activate",self.tab_rename) 
                m.append(rename_item)
                quit_item = gtk.MenuItem("Quit")
                quit_item.connect("activate", lambda discard: gtk.main_quit())	
                quit_item.show()
                m.append(quit_item)
                m.popup(None, None, None, event.button, event.time, None)

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
            if self.str_ == "":
                self.label[pagenum].set_text(self.label[pagenum].get_text())  # eger kullanici string girmezse eski tab adi alinir.
            else:
                self.label[pagenum].set_text(self.str_)
            self.hbox[pagenum].remove(self.entry)
            self.hbox[pagenum].pack_start(self.label[pagenum])
            self.hbox[pagenum].show_all()


    def copy(self, widget=None, data=None):
        pagenum = self.notebook.get_current_page()
        print pagenum 
        if self.terminal.get_has_selection():
            self.terminal.copy_clipboard()

    def paste(self, widget=None, data=None):
        self.terminal.paste_clipboard()

if __name__ == '__main__':
    w = Console()
    gtk.main()



