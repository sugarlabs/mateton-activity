__author__ = "rodripf"
__date__ = "$11/05/2011 09:49:23 AM$"

import pygtk
pygtk.require('2.0')
import gtk

class Numeros:
    def __init__(self):
        self.botones = []
        self.agregar = gtk.Table(4, 3)
        self.agregar.set_row_spacings(2)
        self.agregar.set_col_spacings(2)
        self.agregar.set_size_request(200,200)
        self.agregar.show()

        este = gtk.Button("1")
        self.botones.append(este)
        self.agregar.attach(este, 0, 1, 0, 1)
        

        este = gtk.Button("2")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 0, 1)

        este = gtk.Button("3")
        self.botones.append(este)
        self.agregar.attach(este, 2, 3, 0, 1)

        este = gtk.Button("4")
        self.botones.append(este)
        self.agregar.attach(este, 0, 1, 1, 2)

        este = gtk.Button("5")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 1, 2)

        este = gtk.Button("6")
        self.botones.append(este)
        self.agregar.attach(este, 2, 3, 1, 2)

        este = gtk.Button("7")
        self.botones.append(este)
        self.agregar.attach(este, 0, 1, 2, 3)

        este = gtk.Button("8")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 2, 3)

        este = gtk.Button("9")
        self.botones.append(este)
        self.agregar.attach(este, 2, 3, 2, 3)

        este = gtk.Button("0")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 3, 4)

        este = gtk.Button(",")
        self.botones.append(este)
        self.agregar.attach(este, 2, 3, 3, 4)

        for este in self.botones:
            este.show()
            este.connect("button_press_event", self.__clic)
            
    def setListener(self, functions):
        self.listeners = functions

    def __clic(self, boton, data):
        for f in self.listeners:
            f(boton.get_label())


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    win = gtk.Window(gtk.WINDOW_TOPLEVEL)
    win.set_title("Numeros")
    win.set_border_width(5)
    num = Numeros()
    win.add(num.agregar)
    win.show()
    main()