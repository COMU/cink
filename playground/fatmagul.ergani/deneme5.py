#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk ()

def key(event):
    frame.focus_force()
    print "pressed", repr(event.keysym)


frame = Frame (root, width=100, height=100)

frame.bind("<Key>", key)
frame.pack()
frame.focus_set()

root. mainloop()
