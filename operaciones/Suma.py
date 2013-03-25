__author__="rodripf"
__date__ ="$16/05/2011 08:52:03 AM$"

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


class Suma(Operacion):
    def __init__(self, functions, factores = 3, digitos = 3, correrIDs = 0):
        self.agregar = gtk.HBox()
        self.agregar.show()

        self.principal = gtk.VBox(False, 0)
        self.principal.show()
        self.agregar.pack_end(self.principal)
        
        self.llevo = Factor(digitos, functions, -2)
        self.principal.pack_start(self.llevo.agregar, False, False)

        self.factores = Factores(factores, digitos, functions, True, correrIDs = correrIDs)
        self.principal.pack_start(self.factores.agregar, False, False)

        self.igual = gtk.HBox()
        self.igual.show()
        self.linea = self.getLineaHor(500)
        self.igual.pack_end(self.linea, False, False)        

        self.signo = gtk.Image()
        self.signo.set_from_file("./images/+.gif")
        self.signo.show()
        self.igual.pack_start(self.signo)

        self.principal.pack_start(self.igual, False, True, 10)

        self.resultado = Factor(digitos+1, functions, -1)
        self.principal.pack_start(self.resultado.agregar, False, False)

        self.tipo = 0
        
        self.extra = [self.llevo, self.resultado]

    def comprobar(self):
        if (self.resultado.getValor() == self.factores.sumarTodos()):
            return True
        else:
            return False
            
    def setZoom(self, valor):
        Operacion.setZoom(self, valor)
        if valor == 1 :
            self.llevo.setSize("ss")
            self.llevo.digitos.agregar.set_spacing(0)
        elif valor == 2:
            self.llevo.setSize("ss")
            self.llevo.digitos.agregar.set_spacing(40)
        elif valor == 3:
            self.llevo.setSize("s")
            self.llevo.digitos.agregar.set_spacing(40)
        elif valor == 4:
            self.llevo.setSize("m")
            self.llevo.digitos.agregar.set_spacing(40)
