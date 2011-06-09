__author__="rodripf"
__date__ ="$16/05/2011 08:52:03 AM$"

import pygtk
pygtk.require('2.0')
import gtk

from Operacion import Operacion
from Factores import Factores
from Factor import Factor


class Suma(Operacion):
    def __init__(self, functions, factores = 3, digitos = 3, correrIDs = 0): #para mult si es para multiplicacion
        self.agregar = gtk.HBox()
        self.agregar.show()

        self.principal = gtk.VBox(False, 0)
        self.principal.show()
        self.agregar.pack_end(self.principal)

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

    def comprobar(self):
        if (self.resultado.getValor() == self.factores.sumarTodos()):
            return True
        else:
            return False