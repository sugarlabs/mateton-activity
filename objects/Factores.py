__author__="rodripf"
__date__ ="$06/05/2011 12:08:22 PM$"

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

from Factor import Factor

class Factores():
    def __init__(self, factores, digitos, functions, botonMas = False, unoMenos = False, correrIDs = 0, inverso=False):
        self.defaultListeners = functions
        self.factores = []
        self.agregar = Gtk.HBox()
        self.agregar.show()
        self.inverso = inverso


        self.principal = Gtk.VBox(False, 10)
        self.principal.show()
        self.agregar.pack_end(self.principal, True, True, 0)

        self.correrIDs = correrIDs
        self.digitos = digitos
        self.unoMenos = unoMenos #si voy restando de a uno la cantidad de digitos a medida que agrego
        self.count = 0 + correrIDs #cuenta la cantidad de factores que tengo
       

        self.hided = 0

        for i in range(factores):
            self.agregarUno(self.defaultListeners)

        if botonMas:
            botones = Gtk.VBox()
            botones.show()

            self.botonMenos = Gtk.Button("/\\")
            self.botonMenos.show()
            self.botonMenos.connect("clicked", self.clicMenos)
            botones.pack_start(self.botonMenos, True, True, 0)
            
            self.botonMas = Gtk.Button("\\/")
            self.botonMas.show()
            self.botonMas.connect("clicked", self.clicMas)
            botones.pack_start(self.botonMas, True, True, 0)

            self.agregar.pack_start(botones, False, False, 0)

        


    def agregarUno(self, functions = None):
        if functions == None:
            functions = self.defaultListeners
            
        if self.unoMenos:
            self.digitos -= 1

        if(self.hided == 0):
            este = Factor(self.digitos, functions, self.count, self.inverso)
            if len(self.factores) != 0:
                este.MasListeners = self.factores[0].MasListeners
                este.MenosListeners = self.factores[0].MenosListeners
            self.count += 1
            self.factores.append(este)
            self.principal.pack_start(este.agregar, False, False, 0)
        else:
            self.factores[self.count - self.hided - self.correrIDs].agregar.show()
            self.hided -= 1
        

    def quitarUno(self):
        if self.hided < self.count:
            self.factores[self.count - self.hided - 1 - self.correrIDs].agregar.hide()
            self.hided += 1
        

    def sumarTodos(self):
        res = 0
        for f in self.factores:
            res += f.getValor()
        return res

    def setListener(self, functions):
        for f in self.factores:
            f.setListener(functions)

    def setListenerClicMas(self, functions):
        self.MasListeners = functions

    def clicMas(self, boton):
        self.agregarUno()
        for f in self.MasListeners:
            f()

    def setListenerClicMenos(self, functions):
        self.MenosListeners = functions

    def clicMenos(self, boton):
        self.quitarUno()
        for f in self.MenosListeners:
            f()

    def setListenerFactores(self, functionsClicMas, functionsClicMenos):
        for j in self.factores:
            j.setListenerClicMas(functionsClicMas)
            j.setListenerClicMenos(functionsClicMenos)
            
    def setSize(self, size):
        for f in self.factores:
            f.setSize(size)
