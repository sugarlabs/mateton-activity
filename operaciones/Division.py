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
        self.agregar = gtk.HBox()
        self.agregar.show()

        self.principal = gtk.HBox()
        self.principal.show()
        self.agregar.add(self.principal)

        self.der=gtk.VBox(False, 10)
        self.der.show()
        self.principal.pack_end(self.der, False, False)

        self.linea2 = self.getLineaVer(50)
        self.principal.pack_end(self.linea2, True, True)

        self.izq = gtk.VBox(False, 10)
        self.izq.show()
        self.principal.pack_end(self.izq, False, False)

        self.dividendo = Factor(digitos, functions, digitos)
        self.divisor = Factor(digitos, functions, digitos+1)

        self.cociente = Factor(digitos, functions, -1)
        self.restos = Factores(digitos, digitos, functions, True)

        self.izq.pack_start(self.dividendo.agregar, False, False)
        self.izq.pack_start(self.restos.agregar, False, False)
        self.der.pack_start(self.divisor.agregar, False, False)

        self.igual = gtk.HBox()
        self.igual.show()

        self.linea = self.getLineaHor(200)
        self.igual.pack_end(self.linea, False, False)

        self.der.pack_start(self.igual, False, False)

        self.der.pack_start(self.cociente.agregar, False, False)

        self.factores = self.restos
        self.factores.factores.append(self.dividendo)
        self.factores.factores.append(self.divisor)

        self.resultado = self.cociente
        self.tipo = 3

        self.setZoom(1)