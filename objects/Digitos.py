__author__ = "rodripf"
__date__ = "$06/05/2011 10:56:53 AM$"

import pygtk
pygtk.require('2.0')
import gtk
from Digito import Digito

class Digitos:
    def __init__(self, cant, functions, idFactor):
        self.digitos = []
        self.agregar = gtk.HBox(False)
        self.agregar.show()
        self.defaultListeners = functions
        
        self.idFactor = idFactor
        self.count = 0 #cuenta la cantidad de digitos que tengo

        self.hided = 0
        for i in xrange(cant):
            self.agregarUno(functions)     


    def agregarUno(self, functions = None):
        if functions == None:
            functions = self.defaultListeners
        if(self.hided == 0):
            este = Digito(self.idFactor, self.count)
            self.count += 1
            este.setListener(functions)
            self.digitos.append(este)
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