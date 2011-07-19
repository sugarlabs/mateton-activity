__author__="rodripf"
__date__ ="$30/05/2011 10:24:19 AM$"

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