__author__="rodripf"
__date__ ="$30/05/2011 10:24:19 AM$"

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

from Operacion import Operacion
from Factores import Factores
from Factor import Factor

class Division(Operacion):
    def __init__(self, functions, digitos = 2):
        self.agregar = Gtk.VBox()
        self.agregar.show()
        self.principal = self.agregar

        arriba = Gtk.HBox()
        arriba.show()
        self.agregar.pack_start(arriba, False, False, 0)

        abajo = Gtk.HBox()
        abajo.show()
        self.agregar.pack_start(abajo, False, False, 0)

        self.dividendo = Factor(digitos, functions, 0)
        self.divisor = Factor(digitos, functions, 1)
        self.linea2 = self.getLineaVer(100)

        self.igual = Gtk.HBox()
        self.igual.show()
        self.linea = self.getLineaHor(250)
        self.igual.pack_end(self.linea, True, True, 0)

        arriba.pack_end(self.dividendo.agregar, False, False, 0)
        arriba.pack_end(self.linea2, False, False, 0)
        arriba.pack_end(self.divisor.agregar, False, False, 0)

        self.cociente = Factor(digitos, functions, -1, inverso=True)
        self.restos = Factores(digitos, digitos, functions, True,  correrIDs = 2, inverso=True)

        der = Gtk.VBox()
        der.show()
        der.pack_start(self.igual, False, False, 0)
        der.pack_start(self.cociente.agregar, False, False, 0)

        abajo.pack_end(der, False, False, 0)
        abajo.pack_end(self.restos.agregar, False, False, 0)
        

        

        self.factores = self.restos
        self.factores.factores.insert(0, self.divisor)
        self.factores.factores.insert(0, self.dividendo)

        self.resultado = self.cociente
        self.tipo = 3
        
        self.extra = [self.resultado]
