__author__="rodripf"
__date__ ="$06/05/2011 12:08:22 PM$"

import pygtk
pygtk.require('2.0')
import gtk

from Factor import Factor

class Factores():
    def __init__(self, factores, digitos, functions, botonMas = False, unoMenos = False, correrIDs = 0):
        self.defaultListeners = functions
        self.factores = []
        self.agregar = gtk.HBox()
        self.agregar.show()


        self.principal = gtk.VBox(False, 10)
        self.principal.show()
        self.agregar.pack_end(self.principal)

        self.correrIDs = correrIDs
        self.digitos = digitos
        self.unoMenos = unoMenos #si voy restando de a uno la cantidad de digitos a medida que agrego
        self.count = 0 + correrIDs #cuenta la cantidad de factores que tengo
       

        self.hided = 0

        for i in xrange(factores):
            self.agregarUno(self.defaultListeners)

        if botonMas:
            botones = gtk.VBox()
            botones.show()

            self.botonMenos = gtk.Button("/\\")
            self.botonMenos.show()
            self.botonMenos.connect("clicked", self.clicMenos)
            botones.pack_start(self.botonMenos)
            
            self.botonMas = gtk.Button("\\/")
            self.botonMas.show()
            self.botonMas.connect("clicked", self.clicMas)
            botones.pack_start(self.botonMas)

            self.agregar.pack_start(botones, False, False)

        


    def agregarUno(self, functions = None):
        if functions == None:
            functions = self.defaultListeners
            
        if self.unoMenos:
            self.digitos -= 1

        if(self.hided == 0):
            este = Factor(self.digitos, functions, self.count)
            if len(self.factores) != 0:
                este.MasListeners = self.factores[0].MasListeners
                este.MenosListeners = self.factores[0].MenosListeners
            self.count += 1
            self.factores.append(este)
            self.principal.pack_start(este.agregar, False, False)
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