__author__="rodripf"
__date__ ="$06/05/2011 11:33:20 AM$"

import pygtk
pygtk.require('2.0')
import gtk

from Digitos import Digitos

class Factor:
    def __init__(self, cant, functions, idFactor):
        self.idFactor = idFactor
        self.defaultListeners = functions

        self.MasListeners =()
        self.MenosListeners = ()

        self.botonMas = gtk.Button("<<")
        self.botonMas.show()
        self.botonMas.connect("clicked", self.clicMas)

        self.botonMenos = gtk.Button(">>")
        self.botonMenos.show()
        self.botonMenos.connect("clicked", self.clicMenos)

        self.agregar = gtk.HBox()
        self.agregar.show()

        self.agregar.pack_start(self.botonMas, False, False)
        self.agregar.pack_start(self.botonMenos, False, False)

        self.digitos = Digitos(cant, self.defaultListeners, self.idFactor)
        self.agregar.pack_end(self.digitos.agregar)

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