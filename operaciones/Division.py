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

import pygtk
pygtk.require('2.0')
import gtk

from Operacion import Operacion
from Factores import Factores
from Factor import Factor

class Division(Operacion):
    def __init__(self, functions, digitos = 2):
        self.agregar = gtk.VBox()
        self.agregar.show()
        self.principal = self.agregar

        arriba = gtk.HBox()
        arriba.show()
        self.agregar.pack_start(arriba, False, False)       

        abajo = gtk.HBox()
        abajo.show()
        self.agregar.pack_start(abajo, False, False)

        self.dividendo = Factor(digitos, functions, 0)
        self.divisor = Factor(digitos, functions, 1)
        self.linea2 = self.getLineaVer(100)

        self.igual = gtk.HBox()
        self.igual.show()
        self.linea = self.getLineaHor(250)
        self.igual.pack_end(self.linea)

        arriba.pack_end(self.dividendo.agregar, False, False)
        arriba.pack_end(self.linea2, False, False)
        arriba.pack_end(self.divisor.agregar, False, False)

        self.cociente = Factor(digitos, functions, -1, inverso=True)
        self.restos = Factores(digitos, digitos, functions, True,  correrIDs = 2, inverso=True)

        der = gtk.VBox()
        der.show()
        der.pack_start(self.igual, False, False)
        der.pack_start(self.cociente.agregar, False, False)

        abajo.pack_end(der, False, False)
        abajo.pack_end(self.restos.agregar, False, False)
        

        

        self.factores = self.restos
        self.factores.factores.insert(0, self.divisor)
        self.factores.factores.insert(0, self.dividendo)

        self.resultado = self.cociente
        self.tipo = 3
        
        self.extra = [self.resultado,]
