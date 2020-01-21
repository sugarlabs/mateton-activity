__author__ = "rodripf"
__date__ = "$11/05/2011 09:49:23 AM$"

#      MATETON - Un pizarron para los ninos
#  Copyright (C) 2011 - 2013 Rodrigo Perez Fulloni
#Departamento de Ingenieria, Fundacion Teleton
#             Montevideo, Uruguay
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Numeros:
    def __init__(self):
        self.botones = []
        self.agregar = Gtk.Table(4, 3)
        self.agregar.set_row_spacings(2)
        self.agregar.set_col_spacings(2)
        self.agregar.set_size_request(200,200)
        self.agregar.show()

        este = Gtk.Button("1")
        self.botones.append(este)
        self.agregar.attach(este, 0, 1, 0, 1)
        

        este = Gtk.Button("2")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 0, 1)

        este = Gtk.Button("3")
        self.botones.append(este)
        self.agregar.attach(este, 2, 3, 0, 1)

        este = Gtk.Button("4")
        self.botones.append(este)
        self.agregar.attach(este, 0, 1, 1, 2)

        este = Gtk.Button("5")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 1, 2)

        este = Gtk.Button("6")
        self.botones.append(este)
        self.agregar.attach(este, 2, 3, 1, 2)

        este = Gtk.Button("7")
        self.botones.append(este)
        self.agregar.attach(este, 0, 1, 2, 3)

        este = Gtk.Button("8")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 2, 3)

        este = Gtk.Button("9")
        self.botones.append(este)
        self.agregar.attach(este, 2, 3, 2, 3)

        este = Gtk.Button("0")
        self.botones.append(este)
        self.agregar.attach(este, 1, 2, 3, 4)

        este = Gtk.Button(",")
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
            
    def simularClic(self, valor):
        for f in self.listeners:
            f(valor)


def main():
    Gtk.main()
    return 0

if __name__ == "__main__":
    win = Gtk.Window(Gtk.WindowType.TOPLEVEL)
    win.set_title("Numeros")
    win.set_border_width(5)
    num = Numeros()
    win.add(num.agregar)
    win.show()
    main()
