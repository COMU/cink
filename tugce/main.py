#!/usr/bin/python
from gi.repository import Gtk, Vte
from gi.repository import GLib
import os

vte_list = []

class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.tran_setup()
        self.init_ui()
    
        
    def tran_setup(self):    
        
        self.set_app_paintable(True)  
        screen = self.get_screen()
        
        visual = screen.get_rgba_visual()       
        if visual != None and screen.is_composited():
            self.set_visual(visual)              
        
    def init_ui(self):    

        #self.connect("draw", self.on_draw)        

        self.set_title("test emulator ["+os.environ['HOME']+"]")
        self.resize(600, 280)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.connect("destroy", Gtk.main_quit)


        self.add(TerminalFrame(self))
        self.show_all()

class VteObject(Vte.Terminal):
    def __init__(self, *args, **kwds):
        super(VteObject, self).__init__(*args, **kwds)
        vte_list.append(self)
        self.set_background_saturation(20 / 100.0)
        self.set_opacity(int((100 - 20) / 100.0 * 65535))
        self.fork_command_full(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            [os.environ['SHELL']],
            [],
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )

class TerminalFrame(Gtk.Paned):
    def __init__(self, parent, vte_id = None, *args, **kwds):
        super(TerminalFrame, self).__init__(*args, **kwds) 
        self.vte_id = vte_id
        if self.vte_id == None:
            self.vte = VteObject()
            self.vte_id = len(vte_list)-1
        else:
            self.vte = vte_list[self.vte_id]

        self.add1(self.vte)
        self.menu = Gtk.Menu()

        self.vte.connect("button-release-event", self.button_press)
        self.show_all()

    def button_press(self,widget,event):
        if event.button == 3:
            self.menu = Gtk.Menu()
            self.menu_v_split = Gtk.MenuItem("Split Vertical")
            self.menu_h_split = Gtk.MenuItem("Split Horizontal")

            self.menu_v_split.connect("activate", self.v_split)
            self.menu_h_split.connect("activate", self.h_split)

            self.menu.append(self.menu_v_split)
            self.menu.append(self.menu_h_split)

            #self.menu_v_split.show()
            #self.menu_h_split.show()
            self.menu.show_all()
            self.menu.popup(None, None, None, None, event.button, event.time)
            pass

    def v_split(self, widget):
        self.remove(vte_list[self.vte_id])
        self.set_property('position', self.get_allocation().width / 2)
        self.add1(TerminalFrame(self,self.vte_id)) # old frame
        self.add2(TerminalFrame(self)) # new frame
        self.show_all()

    def h_split(self, widget):
        self.remove(vte_list[self.vte_id])
        vpaned = Gtk.VPaned()
        vpaned.set_property('position', self.get_allocation().height / 2)
        vpaned.add1(TerminalFrame(self,self.vte_id)) # old frame
        vpaned.add2(TerminalFrame(self)) # new frame
        
        self.add1(vpaned)
        vpaned.show_all()
        self.show_all()



def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()
