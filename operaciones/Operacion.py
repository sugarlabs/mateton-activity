__author__ = "rodripf"
__date__ = "$17/05/2011 09:10:57 AM$"

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

import pygtk
pygtk.require('2.0')
import gtk

class Operacion:
    tipo = None
    factores = None
    resultado = None


    def setZoom(self, valor):
        size = ""

        if valor == 1:
            size = "ss"
            self.factores.principal.set_spacing(5)
            self.principal.set_spacing(10)
        elif valor == 2:
            size = "s"
            self.factores.principal.set_spacing(10)
            self.principal.set_spacing(20)
        elif valor == 3:
            size = "m"
            self.factores.principal.set_spacing(20)
            self.principal.set_spacing(40)
        elif valor == 4:
            self.factores.principal.set_spacing(40)
            self.principal.set_spacing(80)
            size = "l"



        self.factores.setSize(size)            
        self.resultado.setSize(size)


    def setValor(self, factor, digito, valor):
        if (factor >= 0):
            self.factores.factores[factor].digitos.digitos[digito].setValor(valor)
        else:
            self.extra[factor].digitos.digitos[digito].setValor(valor)      


    def getLineaHor(self, largo):
        im = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("./images/lineaHor.png")
        scaled_buf = pixbuf.scale_simple(largo, 3, gtk.gdk.INTERP_BILINEAR)
        im.set_from_pixbuf(scaled_buf)
        im.show()
        return im

    def actualizarLineHor(self, data1):
#        self.igual.remove(self.linea)
#        rect = self.igual.get_allocation()
#        self.linea = self.getLineaHor(rect.width)
#        self.igual.add(self.linea)
        pass

    def getLineaVer(self, alto):
        im = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("./images/lineaVer.png")
        scaled_buf = pixbuf.scale_simple(3, alto, gtk.gdk.INTERP_BILINEAR)
        im.set_from_pixbuf(scaled_buf)
        im.show()
        return im
