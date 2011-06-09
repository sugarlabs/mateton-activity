__author__="rodripf"
__date__ ="$27/05/2011 11:29:52 AM$"

import pygtk
pygtk.require('2.0')
import gtk

from Operacion import Operacion
from Factores import Factores
from Factor import Factor


class Resta(Operacion):
    def __init__(self, functions, digitos = 3):
        self.agregar = gtk.VBox()
        self.agregar.show()

        self.principal = gtk.VBox()
        self.principal.show()
        self.agregar.pack_start(self.principal, False, False)

        self.factores = Factores(2, digitos, functions, False)
        self.principal.pack_start(self.factores.agregar, False, False)

        self.igual = gtk.HBox()
        self.igual.show()
        self.linea = self.getLineaHor(500)
        self.igual.pack_end(self.linea, False, False)

        self.signo = gtk.Image()
        self.signo.set_from_file("./images/-.gif")
        self.signo.show()
        self.igual.pack_start(self.signo, False, False)

        self.principal.pack_start(self.igual, False, False)

        self.resultado = Factor(digitos+1, functions, -1)
        self.principal.pack_start(self.resultado.agregar, False, False)

        self.tipo = 1

    def comprobar(self):
        pass