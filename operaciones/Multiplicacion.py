__author__="rodripf"
__date__ ="$27/05/2011 11:33:41 AM$"

import pygtk
pygtk.require('2.0')
import gtk

from Operacion import Operacion
from Factores import Factores
from Suma import Suma


class Multiplicacion(Operacion):
    def __init__(self, functions, digitos = 2):
        self.agregar = gtk.HBox()
        self.agregar.show()

        self.principal = gtk.VBox()
        self.principal.show()
        self.agregar.pack_end(self.principal)

        self.factores = Factores(2, digitos, functions, False)
        self.principal.pack_start(self.factores.agregar, False, False)

        self.igual = gtk.HBox()
        self.igual.show()
        self.linea = self.getLineaHor(500)
        self.igual.pack_end(self.linea, False, False)

        self.signo = gtk.Image()
        self.signo.set_from_file("./images/x.gif")
        self.signo.show()
        self.igual.pack_start(self.signo)

        self.principal.pack_start(self.igual, False, False)

        
        self.suma = Suma(functions, digitos, digitos, 2)
        self.principal.pack_start(self.suma.agregar, False, False)

        self.factores.factores.extend(self.suma.factores.factores)

        self.resultado = self.suma.resultado
        
        self.tipo = 2

    def comprobar(self):
        if (self.resultado.getValor() == self.factores.sumarTodos()):
            return True
        else:
            return False



