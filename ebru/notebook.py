import gtk 
import vte
import os
import gobject
import time
import keybinder
from utils import Utils
from vteTerminal import VteTerminal

class Console(Utils,VteTerminal):
    def __init__(self):
	self.win = gtk.Window()
        self.win.connect('delete-event', lambda win, event: gtk.main_quit())
        self.base_setting()
	keybinder.bind(self.window_open_key,self.callback,None)
	print "F10 bas"
        self.shortcut()
	self.win.add(self.notebook)  
        self.vteObj = VteTerminal()
	self.vteObj.constr()
        # sag tiklama icin uc arg verildi
#        self.create_tab(widget=None,data=None) 

    def callback(self,user_data):
	print 	"F10 basildi"	
	if not self.window_open:
		print "pencere suan kapali pencereyi ac"
		self.create_tab(widget=None,data=None)
		self.window_open = True
	else:
		self.window_open = False
		print "Pencere acik pencereyi kapat"
		o = Shrink()
		if self.direction == "left":
			o.shrink_left(self.win)
		elif self.direction == "right":
			o.shrink_right(self.win)
		elif self.direction == "down":
			o.shrink_down(self.win)
		
    def variable(self):
	self.window_open_key = "F10"
	self.window_open = False
        # bu degiskeni sadece ilk sayfa kapatildiginda baska sayfalarda varsa pencereyi tamamen kapatilmasin diye
        self.page_ = 0
	self.is_first=0 #pencerenin ilk acilma bilgisi
        self.label = [] # tab isimleri
        self.hbox = [] # acilan her tabin hboxi
        """ etiket ve sekme indexleri dizide tutuldugu icin her sekme
        acilip kapandiginda dizi indexinde problem olmasin diye"""
    # temel notebook icin yuklenilmesi gerekenler
    def base_setting(self):
        self.variable()	
	self.win.set_resizable(True)
	self.win.set_decorated(False)
        self.notebook = gtk.Notebook()
        # cok fazla sekme acilinca kaydirma cubugu
        self.notebook.set_scrollable(True) 
        self.notebook.set_tab_pos(gtk.POS_BOTTOM)
 
    def create_tab(self,widget=None,data=None):
        self.page_ += 1 
	self.vteObj.index_ = len(self.hbox)
        self.hbox.append(gtk.HBox(False, 0))
        self.hbox[self.vteObj.index_].set_spacing(1)
        # kullanici labelleri degistirebilsin diye diziye atildi
        self.tab_name_no()
        self.hbox[self.vteObj.index_].pack_start(self.label[self.vteObj.index_])
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
        self.hbox[self.vteObj.index_].pack_end(btn, False, False)
        # kapatma butonunun boyutunun ayarlanmasi icin
        style = gtk.RcStyle()
        style.xthickness = 0
        style.ythickness = 0
        btn.modify_style(style)
        self.hbox[self.vteObj.index_].show_all()
        # yeni terminal olusturulmasi
        self.vteObj.terminal_setting()
        self.vteObj.terminal_action()
        self.notebook.insert_page(self.vteObj.terminal[self.vteObj.index_],self.hbox[self.vteObj.index_])
	self.vteObj.terminal[self.vteObj.index_].connect('event',self.right_click)
        self.notebook.set_current_page(self.page_-1)
	#sadece terminal ilk acildiginda kayarak ilerleme yapmasi
	if self.is_first == 0:
		self.is_first =1
		o = Expand()
		self.direction = "left"
		if self.direction== "down":
			self.win.set_size_request(500,50)
			self.win.move((gtk.gdk.screen_width()-500)/2,0)
			o.expand_down(self.win)
		elif self.direction == "right":
			self.win.move(0,0)
			o.expand_right(self.win)
		elif self.direction == "left":
			self.win.move(gtk.gdk.screen_width(),0)
			o.expand_left(self.win)
	self.win.show_all()
    
    def full_screen(self,accelgroup,win,key,mod):
        if self.is_fullscreen == False:
            self.win.fullscreen()
            self.is_fullscreen = True
        elif self.is_fullscreen == True:
            self.win.unfullscreen()
     	    self.win.resize(400,400)
            self.is_fullscreen = False

    def shortcut(self):
    	accelgroup = []
	# full screen
        accelgroup.append(gtk.AccelGroup())
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
        self.win.add_accel_group(accelgroup[0])
        self.win.add_accel_group(accelgroup[1])
        self.win.add_accel_group(accelgroup[2]) 
    
class Expand():
	def expand_down(self,win):
		for i in range(50,500):
			win.set_size_request(500,i)
			win.show_all()
			while gtk.events_pending():
		        	gtk.main_iteration(block=False)
	                time.sleep(0.01)
	def expand_right(self,win):
		for i in range(50,500):
			win.set_size_request(i,500)
			win.show_all()
			while gtk.events_pending():
                        	gtk.main_iteration(block=False)
                        time.sleep(0.01)
	def expand_left(self,win):
		for i in range(50,500):
                        win.set_size_request(i,500)
                        win.show_all()
                        while gtk.events_pending():
                                gtk.main_iteration(block=False)
                        time.sleep(0.01)		

class Shrink():
	def shrink_down(self,win):
		pass
	def shrink_right(self,win):
		pass
	def shrink_left(self,win):
		print "kucult"
		win.set_default_size(300,300)
		win.show_all()
		print win.get_size()
		"""
		for i in range(500,50,-1):
			print i
			win.set_size_request(i,i)
			
			win.show_all()
			print win.get_size()
			while gtk.events_pending():
                                gtk.main_iteration(block=False)
                        time.sleep(0.01)
		"""

def main():
    app = Console()
    gtk.main()

if __name__ == "__main__":
    main()

