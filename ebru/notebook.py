import gtk 
import vte
import os

win = gtk.Window()
class Console():
    def __init__(self):
        win.connect('delete-event', lambda win, event: gtk.main_quit())
        self.base_setting()
        win.add(self.notebook)  
        self.create_tab(widget=None,data=None) #sag tiklamayla aktif olsun diye uc tane arg verildi

    def base_setting(self):
        self.page_ = 1 # tab sayfalari icin
        self.label = [] # tab isimleri
        self.hbox = []
        win.resize(400,400)
        self.notebook = gtk.Notebook()
        # cok fazla sekme acilinca kaydirma cubugu
        self.notebook.set_scrollable(True) 
        self.notebook.set_tab_pos(gtk.POS_BOTTOM)

    def create_tab(self,widget=None,data=None):
        self.page_ = self.page_+1
        self.index_ = self.page_-2 
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
        # yeni terminal olusturulmasi
        self.terminal_action()
        self.notebook.insert_page(self.terminal,self.hbox[self.index_])
         # sekme kapatmak icin fonksiyonun aktif edilmesi
#        btn.connect('clicked', self.close_tab)
        # yeni sekme acildiginda gostermesi icin
        win.show_all() 
        # yeni sekme acildiginda direkt o sekmeye gecsin diye
        self.notebook.set_current_page(self.page_-2) 

    def create_terminal(self):
        self.argv = ['bash']
        self.env = self.env_map_to_list(os.environ.copy())
        self.cwd = os.environ['HOME']
        self.is_fullscreen = False
        self.terminal = vte.Terminal()
        self.terminal.set_colors(gtk.gdk.color_parse('white'),gtk.gdk.color_parse('pink'),[])
        #self.terminal.set_background_transparent(1)

    def terminal_action(self):
        self.create_terminal()
        self.terminal.fork_command(self.argv[0], self.argv, self.env, self.cwd)
        return self.terminal

    def env_map_to_list(self, env): # terminal fork_command icin
        return ['%s=%s' % (k, v) for (k, v) in env.items()]



if __name__ == '__main__':
    w = Console()
    gtk.main()

