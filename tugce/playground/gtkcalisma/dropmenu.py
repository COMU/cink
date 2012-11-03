import gtk
import time
class Pencere(object):
	def __init__(self):
		self.pencere = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.pencere.set_title("Pencere")
		self.buton = gtk.Button("kapat")
		self.pencere.set_border_width(10)
		self.buton.show()
		self.pencere.add(self.buton)
		#self.pencere.resize(400,200)
		self.pencere.move(300,400)
		self.buton.connect("clicked",gtk.main_quit)
		#self.pencere.connect("delete_event",gtk.main_quit)
		self.pencere.set_opacity(0.9)
		self.pencere.show()
		
	def main(self):
		gtk.main()

ilk = Pencere()
ilk.main()
