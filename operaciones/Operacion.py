__author__ = "rodripf"
__date__ = "$17/05/2011 09:10:57 AM$"

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



        for f in self.factores.factores:
                for d in f.digitos.digitos:
                        d.setSize(size)
        for d in self.resultado.digitos.digitos:
            d.setSize(size)




    def setValor(self, factor, digito, valor):
        if (factor >= 0):
            self.factores.factores[factor].digitos.digitos[digito].setValor(valor)
        else:
            self.resultado.digitos.digitos[digito].setValor(valor)

    def getLineaHor(self, largo):
        im = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("./images/lineaHor.png")
        scaled_buf = pixbuf.scale_simple(largo, 3, gtk.gdk.INTERP_BILINEAR)
        im.set_from_pixbuf(scaled_buf)
        im.show()
        return im

    def actualizarLineHor(self, data1):
        self.igual.remove(self.linea)
        rect = self.igual.get_allocation()
        self.linea = self.getLineaHor(rect.width)
        self.igual.add(self.linea)

    def getLineaVer(self, alto):
        im = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("./images/lineaVer.png")
        scaled_buf = pixbuf.scale_simple(3, alto, gtk.gdk.INTERP_BILINEAR)
        im.set_from_pixbuf(scaled_buf)
        im.show()
        return im