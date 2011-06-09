__author__="rodripf"
__date__ ="$27/04/2011 11:42:02 AM$"


import pygtk
pygtk.require('2.0')
import gtk

class Digito:
    #Crea un digito en particular. self.agregar es el widget gtk para agregar a
    #la ventana

    def __init__(self, idFactor, idDigito):
        self.size = "s"
        self.anim = gtk.gdk.PixbufAnimation("./images/" + self.size + "/" + "-1.gif")
        self.img = gtk.Image()
        self.img.set_from_animation(self.anim)
        self.iter = self.anim.get_iter()
        self.img.show()

        self.agregar = gtk.EventBox()
        self.agregar.show()
        self.agregar.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.agregar.connect("button_press_event", self.__clic)
        
        self.agregar.add(self.img)
        self.selected = False;

        self.idFactor = idFactor
        self.idDigito = idDigito

        self.valor = -1


    def setValor(self, valor):
        self.valor = valor
        self.anim = gtk.gdk.PixbufAnimation("./images/"+ self.size + "/" + str(valor) + ".gif")
        self.img.set_from_animation(self.anim)

    def setSize(self, size):
        self.size = size
        self.selected = False
        self.anim = gtk.gdk.PixbufAnimation("./images/"+ self.size + "/" + str(self.valor) + "_s.gif")
        self.img.set_from_animation(self.anim)


    def getValor(self):
        return self.valor
        
    def setListener(self, functions):
        self.listeners = functions
        
    def __clic(self, button, otro):
        for f in self.listeners:
            f(self)

    def seleccionar(self, si):
        if not si:
            self.selected = False
            self.anim = gtk.gdk.PixbufAnimation("./images/"+ self.size + "/" + str(self.valor) + "_s.gif")
            self.img.set_from_animation(self.anim)
        else:
            self.selected = True
            self.anim = gtk.gdk.PixbufAnimation("./images/"+ self.size + "/" + str(self.valor) + "_r.gif")
            self.img.set_from_animation(self.anim)