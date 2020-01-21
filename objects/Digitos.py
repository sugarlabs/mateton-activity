__author__ = "rodripf"
__date__ = "$06/05/2011 10:56:53 AM$"

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
from Digito import Digito

class Digitos:
    def __init__(self, cant, functions, idFactor, inverso=False):
        self.digitos = []
        self.agregar = Gtk.HBox(False)
        self.agregar.show()
        self.defaultListeners = functions
        self.inverso = inverso
        
        self.idFactor = idFactor
        self.count = 0 #cuenta la cantidad de digitos que tengo

        self.hided = 0
        for i in range(cant):
            self.agregarUno(functions)     


    def agregarUno(self, functions = None):
        if functions == None:
            functions = self.defaultListeners

        if(self.hided == 0):
            este = Digito(self.idFactor, self.count)
            self.count += 1
            este.setListener(functions)
            self.digitos.append(este)
            
            if self.inverso:
                self.agregar.pack_start(este.agregar, False, False, 10)
            else:
                self.agregar.pack_end(este.agregar, False, False, 10)
                    

                
        else:
            self.digitos[self.count - self.hided].agregar.show()
            self.hided -= 1

    def quitarUno(self):
        if self.hided < self.count:
            self.digitos[self.count - self.hided -1].agregar.hide()
            self.hided += 1



    def obtenerNumero(self):
        i=len(self.digitos)
        res = 0
        for dig in self.digitos:
            res += dig.getValor()*10^i
            i-=1
        return res

    def setListener(self, functions):
        for d in self.digitos:
            d.setListener(functions)
            
    def setSize(self, size):
        for dig in self.digitos:
            dig.setSize(size)      
