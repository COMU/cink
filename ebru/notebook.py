import gtk 
import vte
import os
import gobject
from utils import Utils

win = gtk.Window()
class Console(Utils):
    def __init__(self):
        win.connect('delete-event', lambda win, event: gtk.main_quit())
        self.base_setting()
        self.shortcut()
        win.add(self.notebook)  
        # sag tiklama icin uc arg verildi
        self.create_tab(widget=None,data=None) 
    
    def variable(self):
        # bu degiskeni sadece ilk sayfa kapatildiginda baska sayfalarda varsa pencereyi tamamen kapatilmasin diye
        self.page_ = 0
        self.label = [] # tab isimleri
        self.hbox = [] # acilan her tabin hboxi
        self.terminal = []
        """ etiket ve sekme indexleri dizide tutuldugu icin her sekme
        acilip kapandiginda dizi indexinde problem olmasin diye"""
        self.index_ = -1
    # temel notebook icin yuklenilmesi gerekenler
    def base_setting(self):
        self.variable()	
	win.set_resizable(True)
	win.set_decorated(False)
        self.notebook = gtk.Notebook()
	width, height = win.get_size()
	win.move((gtk.gdk.screen_width()-width)/2-150, 0)	
        # cok fazla sekme acilinca kaydirma cubugu
        self.notebook.set_scrollable(True) 
        self.notebook.set_tab_pos(gtk.POS_BOTTOM)

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

    def create_tab(self,widget=None,data=None):
        self.page_ += 1 
        self.index_ = len(self.hbox)
        self.hbox.append(gtk.HBox(False, 0))
        self.hbox[self.index_].set_spacing(1)
        # kullanici labelleri degistirebilsin diye diziye atildi
        self.tab_name_no()

        #self.label.append(gtk.Label("tab"+str(self.index_+1)))  
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
        # yeni terminal olusturulmasi
        self.terminal_setting()
        self.terminal_action()
        self.notebook.insert_page(self.terminal[self.index_],self.hbox[self.index_])
        self.notebook.set_current_page(self.page_-1)
	i=1	
	win.set_default_size(0,0)

    def terminalSize(self):
	for i in range(1,gtk.gdk.screen_height()):
                win.resize(300,i)
		print win.get_size()
		print i
		i+=1
                win.show_all()
			
    def terminal_setting(self):
        self.argv = ['bash']
        self.env = self.env_map_to_list(os.environ.copy())
        self.cwd = os.environ['HOME']
        self.is_fullscreen = False
        self.terminal.append(vte.Terminal())
        # self.index_ sekme sayfasiyla ayni
        self.terminal[self.index_].set_colors(gtk.gdk.color_parse('white'),gtk.gdk.color_parse('pink'),[])
        #self.terminal.set_background_transparent(1)

    def terminal_action(self):
        self.terminal[self.index_].fork_command(self.argv[0], self.argv, self.env, self.cwd)
        self.terminal[self.index_].connect('event',self.right_click)
        return self.terminal[self.index_]

    def env_map_to_list(self, env): # terminal fork_command icin
        return ['%s=%s' % (k, v) for (k, v) in env.items()]

    def full_screen(self,accelgroup,win,key,mod):
        if self.is_fullscreen == False:
            win.fullscreen()
            self.is_fullscreen = True
        elif self.is_fullscreen == True:
            win.unfullscreen()
	    win.resize(400,400)
	    print win.get_size()
            self.is_fullscreen = False



if __name__ == '__main__':
    w = Console()
    gobject.idle_add(w.terminalSize)
    gtk.main()
