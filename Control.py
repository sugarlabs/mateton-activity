#!/usr/bin/env python

# example helloworld2.py

import pygtk
pygtk.require('2.0')
import gtk
import sys

sys.path.append('./objects')
sys.path.append('./operaciones')
sys.path.append('./historia')
sys.path.append('./data')

from Suma import Suma
from Resta import Resta
from Multiplicacion import Multiplicacion
from Division import Division
from Numeros import Numeros
from Menu import Menu
from Historia import Historia
from Suceso import Suceso
from Manager import Manager
from EstadoOperacion import EstadoOperacion

class Control:
    def deleteEvent(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        #variable initialization
        self.seleccionado = None
        self.guardado = False
        self.hist = Historia()
        self.cuenta = None
        self.zoom =2
        
        #Contiene todo
        self.todo = gtk.HBox(False, 0)
        self.todo.show()
        

        #Contiene los menus
        self.menus = gtk.VBox(False, 0)
        self.menus.show()
        self.todo.pack_start(self.menus, False, False)

        #Contiene el pizarron
        self.pizarron = gtk.ScrolledWindow()
        self.pizarron.show()
      
        self.cargarCuenta(0)

        self.todo.add(self.pizarron)

        self.num = Numeros()
        self.menus.add(self.num.agregar)

        self.menu = Menu()
        self.menus.add(self.menu.agregar)
        self.menu.setDeshacerListeners((self.__deshacer,))
        self.menu.setHistListeners((self.__moverHistoria,))
        self.menu.setSumaListeners((self.__suma,))
        self.menu.setRestaListeners((self.__resta,))
        self.menu.setDivisionListeners((self.__division,))
        self.menu.setMultiplicacionListeners((self.__multiplicacion,))
        self.menu.setZoomListeners((self.__moverZoom, self.cuenta.actualizarLineHor))
        self.menu.setBorrarListeners((self.__agregarAHistCV, self.__numClic, self.__actualizarAdj))

        

        #registro listeners
        self.num.setListener((self.__agregarAHistCV, self.__numClic, self.__actualizarAdj))

        self.mngr = Manager((self.__digClic,))
        self.menu.setGuardarListeners((self.mantener,))
        self.menu.setAbrirListeners((self.cargar,))

        # Create a new window

        #<uncomment for PC>


#        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#        self.window.set_title("Mateton")
#        self.window.connect("delete_event", self.deleteEvent)
#        self.window.set_border_width(5)
#        self.window.set_default_size(800, 600)
#
#        self.window.add(self.todo)
#        self.window.show()



        #</uncomment for PC>

    def cargarCuenta(self, tipo, operacion=None):
        if self.seleccionado != None:
            self.__desseleccionar()
        if not self.cuenta == None:
            self.todo.remove(self.pizarron)
            self.pizarron = gtk.ScrolledWindow()
            self.pizarron.show()
            self.todo.add(self.pizarron)
            del self.cuenta

            del self.hist
            self.hist = Historia()
            self.__actualizarAdj()

        if not operacion== None:
            self.cuenta = operacion
        else:
            if tipo == 0:
                self.cuenta = Suma((self.__digClic,))
            elif tipo==1:
                self.cuenta = Resta((self.__digClic,))
            elif tipo == 2:
                self.cuenta = Multiplicacion((self.__digClic,))
            elif tipo==3:
                self.cuenta = Division((self.__digClic,))

        if tipo == 0 or tipo == 1:
            self.cuenta.factores.setListenerClicMas((self.__agregarAHistAF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.factores.setListenerClicMenos((self.__agregarAHistQF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.factores.setListenerFactores((self.__agregarAHistAD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom), (self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.resultado.setListenerClicMas((self.__agregarAHistAD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.resultado.setListenerClicMenos((self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
        elif tipo == 2:
            self.cuenta.factores.setListenerClicMas((self.__agregarAHistAF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.factores.setListenerClicMenos((self.__agregarAHistQF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.factores.setListenerFactores((self.__agregarAHistAD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom), (self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))

            self.cuenta.suma.factores.setListenerFactores((self.__agregarAHistAD, self.__actualizarAdj, self.__moverZoom), (self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.suma.factores.setListenerClicMenos((self.__agregarAHistQF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.suma.factores.setListenerClicMas((self.__agregarAHistAF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom, self.__actualizarFactores))

            self.cuenta.suma.resultado.setListenerClicMas((self.__agregarAHistAD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.suma.resultado.setListenerClicMenos((self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))

        elif tipo == 3:
            self.cuenta.restos.setListenerClicMas((self.__agregarAHistAF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.restos.setListenerClicMenos((self.__agregarAHistQF, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.restos.setListenerFactores((self.__agregarAHistAD, self.__actualizarAdj, self.__moverZoom), (self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))

            self.cuenta.cociente.setListenerClicMas((self.__agregarAHistAD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.cociente.setListenerClicMas((self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar))

            self.cuenta.divisor.setListenerClicMas((self.__agregarAHistAD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.divisor.setListenerClicMas((self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))

            self.cuenta.dividendo.setListenerClicMas((self.__agregarAHistAD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))
            self.cuenta.dividendo.setListenerClicMas((self.__agregarAHistQD, self.__actualizarAdj, self.__desseleccionar, self.__moverZoom))

        self.pizarron.add_with_viewport(self.cuenta.agregar)
        print "paso"


    def __numClic(self, valor): #callback para clic en boton numero
        if self.seleccionado:
            self.seleccionado.setValor(valor)

    def __digClic(self, digito): #callback para clic en digitos
        if self.seleccionado != digito:
            if self.seleccionado != None:
                self.seleccionado.seleccionar(False)
            self.seleccionado = digito
            self.seleccionado.seleccionar(True)

    def __agregarAHistCV(self, valor): #callback para clic en boton numero
         if self.seleccionado and self.seleccionado.getValor() != valor:
            suc = Suceso(0)
            suc.setObjeto(self.seleccionado.idFactor, self.seleccionado.idDigito)
            suc.setValor((self.seleccionado.getValor(), valor))
            self.hist.agregar(suc)

    def __agregarAHistAF(self): #callback para agregar factor
        suc = Suceso(1)
        self.hist.agregar(suc)

    def __agregarAHistQF(self): #callback para quitar factor
        suc = Suceso(2)
        self.hist.agregar(suc)

    def __agregarAHistAD(self, idFactor):
        suc = Suceso(3)
        suc.setObjeto(idFactor)
        self.hist.agregar(suc)

    def __agregarAHistQD(self, idFactor):
        suc = Suceso(4)
        suc.setObjeto(idFactor)
        self.hist.agregar(suc)

    def __actualizarAdj(self, data1=0, data2=0):
        self.menu.cargarAdj(self.hist.getPosicion()+1, 0, len(self.hist.suc)-1)
        self.menu.setHistListeners((self.__moverHistoria,))
       

    def __deshacer(self, boton, data): #callback para el boton deshacer
        self.hist.setPosicion(self.hist.getPosicion()-1, self.cuenta)
        self.menu.adj.set_value(self.hist.getPosicion())



    def __moverHistoria(self, obj): #callback el slider
        valor = obj.get_value()
        if valor != self.hist.getPosicion():
            self.hist.setPosicion(int(round(valor)), self.cuenta)

    def __moverZoom(self, obj=None, data=0): #callback el slider
        if obj!=None:
            try:
                self.zoom = obj.get_value()
            except:
                pass

        self.cuenta.setZoom(self.zoom)

    def mantener(self, obj = None, data =None, nombre = ""): #callback para boton guardar
        if (nombre != ""):
            self.mngr.setArchivo(nombre)
        else:
            self.mngr.setArchivo("prueba1")

        self.guardado = True
        self.mngr.setHistoria(self.hist)
        estado = EstadoOperacion(self.cuenta)
        self.mngr.setEstadoOperacion(estado)
        self.mngr.guardar()

    def cargar(self, obj = None, data = None, nombre = ""): #callback para boton cargar
        if (nombre != ""):
            self.mngr.setArchivo(nombre)
        else:
            self.mngr.setArchivo("prueba1")
        (hist, op) = self.mngr.abrir()
        self.cargarCuenta(op.tipo, op)
        self.hist = hist        
        self.__actualizarAdj()

    def __suma(self, obj, data):
        self.cargarCuenta(0)

    def __resta(self, obj, data):
        self.cargarCuenta(1)

    def __multiplicacion(self, obj, data):
        self.cargarCuenta(2)

    def __division(self, obj, data):
        self.cargarCuenta(3)

    def __desseleccionar(self, obj=0, data=0):
        if self.seleccionado != None:
            self.seleccionado.seleccionar(False)
            self.seleccionado = None

    def __actualizarFactores(self):
        """Solucion chancha. Solo para multiplicaciones. Agrega el nuevo factor de la
        suma a la lista de factores"""
        self.cuenta.factores.factores.append(self.cuenta.suma.factores.factores[len(self.cuenta.suma.factores.factores)-1])




def main():
    gtk.main()

if __name__ == "__main__":
    hello = Control()
    main()