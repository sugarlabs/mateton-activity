__author__="rodripf"
__date__ ="$06/05/2011 11:33:20 AM$"

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

from Digitos import Digitos

class Factor:
    def __init__(self, cant, functions, idFactor, inverso=False):
        self.idFactor = idFactor
        self.defaultListeners = functions

        self.MasListeners =()
        self.MenosListeners = ()

        self.botonMas = Gtk.Button("<<")
        self.botonMas.show()
        self.botonMas.connect("clicked", self.clicMas)

        self.botonMenos = Gtk.Button(">>")
        self.botonMenos.show()
        self.botonMenos.connect("clicked", self.clicMenos)

        self.agregar = Gtk.HBox()
        self.agregar.show()

        self.agregar.pack_start(self.botonMas, False, False, 0)
        self.agregar.pack_start(self.botonMenos, False, False, 0)

        self.digitos = Digitos(cant, self.defaultListeners, self.idFactor, inverso)
        self.agregar.pack_end(self.digitos.agregar, True, True, 0)

        self.setListener(functions)       

    def setListener(self, functions):
        self.digitos.setListener(functions)

    def getValor(self):
        return self.digitos.obtenerNumero()

    def setListenerClicMas(self, functions):
        self.MasListeners = functions

    def clicMas(self, boton):
        self.digitos.agregarUno()
        for f in self.MasListeners:
            f(self.idFactor)

    def setListenerClicMenos(self, functions):
        self.MenosListeners = functions

    def clicMenos(self, boton):
        self.digitos.quitarUno()
        for f in self.MenosListeners:
            f(self.idFactor)
            
    def setSize(self, size):
        self.digitos.setSize(size)
