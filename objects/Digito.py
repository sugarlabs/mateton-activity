__author__="rodripf"
__date__ ="$27/04/2011 11:42:02 AM$"

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
from gi.repository import Gtk, GdkPixbuf, Gdk


class Digito:
    #Crea un digito en particular. self.agregar es el widget gtk para agregar a
    #la ventana

    def __init__(self, idFactor, idDigito):
        self.size = "s"
        self.anim = GdkPixbuf.PixbufAnimation.new_from_file("./images/" + self.size + "/" + "-1.gif")
        self.img = Gtk.Image()
        self.img.set_from_animation(self.anim)
        self.iter = self.anim.get_iter()
        self.img.show()

        self.agregar = Gtk.EventBox()
        self.agregar.show()
        self.agregar.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.agregar.connect("button_press_event", self.__clic)
        
        self.agregar.add(self.img)
        self.selected = False;

        self.idFactor = idFactor
        self.idDigito = idDigito

        self.valor = -1


    def setValor(self, valor):
        self.valor = valor
        self.anim = GdkPixbuf.PixbufAnimation.new_from_file("./images/"+ self.size + "/" + str(valor) + ".gif")
        self.img.set_from_animation(self.anim)

    def setSize(self, size):
        self.size = size
        self.selected = False
        self.anim = GdkPixbuf.PixbufAnimation.new_from_file("./images/"+ self.size + "/" + str(self.valor) + "_s.gif")
        self.img.set_from_animation(self.anim)


    def getValor(self):
        return self.valor
        
    def setListener(self, functions):
        self.listeners = functions
        
    def __clic(self, button, otro):
        for f in self.listeners:
            f(self)

    def seleccionar(self, si):
        if not si:
            self.selected = False
            self.anim = GdkPixbuf.PixbufAnimation.new_from_file("./images/"+ self.size + "/" + str(self.valor) + "_s.gif")
            self.img.set_from_animation(self.anim)
        else:
            self.selected = True
            self.anim = GdkPixbuf.PixbufAnimation.new_from_file("./images/"+ self.size + "/" + str(self.valor) + "_r.gif")
            self.img.set_from_animation(self.anim)
