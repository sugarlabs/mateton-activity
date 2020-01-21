__author__="rodripf"
__date__ ="$12/05/2011 09:49:53 AM$"

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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gettext import gettext as _

class Menu:
    def __init__(self):
        self.agregar = Gtk.VBox()
        self.agregar.show()
        
#<uncomment for PC>

#        #Guardar y cargar
        #herr = Gtk.Frame(_("Tools"))
        #herr.show()
        #cont1 = Gtk.VBox(False, 5)
        #cont1.show()
        #h3 = Gtk.VBox(False, 5)
        #h3.show()
        #h4 = Gtk.HBox()
        #h4.show()

#</uncomment for PC>

        self.adj = None
        self.history = None

        #Deshacer y borrar
        
        herr = Gtk.Frame.new(_("Tools"))
        herr.show()
        cont1 = Gtk.VBox(False, 5)
        cont1.show()
        h3 = Gtk.VBox()
        h3.show()
        h4 = Gtk.HBox()
        h4.show()


        
        self.borrar = Gtk.Button(_("Erase"))
        self.borrar.connect("button_press_event", self.__clicBorrar)
        self.borrar.show()
        h3.add(self.borrar)

#<uncomment for PC>
        #self.keep = Gtk.Button(_("Save"))
        #self.keep.show()
        #h3.add(self.keep)


        #self.open = Gtk.Button(_("Load"))
        #self.open.show()
        #h3.add(self.open)
#</uncomment for PC>

        
        h = Gtk.Frame.new(_("History"))
        h.show()
        h3.add(h)
        self.cont2 = Gtk.VBox()
        self.cont2.show()
        h.add(self.cont2)

        self.undo = Gtk.Button(_("Undo"))
        self.undo.show()
        self.cont2.add(self.undo)

        self.cargarAdj(0, 0, 0, 1, 1)

        z = Gtk.Frame.new(_("Zoom"))
        z.show()
        h3.add(z)
        self.adj2 = Gtk.Adjustment(2, 1, 4, 1, 1)
        self.zoom = Gtk.HScale.new(self.adj2)
        self.zoom.set_digits(0)
        self.zoom.show()
        z.add(self.zoom)
        
        cont1.add(h3)
        cont1.add(h4)
        herr.add(cont1)
        

        #Operaciones
        oper = Gtk.Frame.new(_("Start new operation"))
        oper.show()
        cont = Gtk.VBox(False, 5)
        cont.show()
        h1 = Gtk.HBox()
        h1.show()
        h2 = Gtk.HBox()
        h2.show()

        self.suma = Gtk.Button(_("Addition"))
        self.suma.show()
        h1.add(self.suma)
        self.resta = Gtk.Button(_("Subtraction"))
        self.resta.show()
        h1.add(self.resta)
        self.mult = Gtk.Button(_("Multiplication"))
        self.mult.show()
        h2.add(self.mult)
        self.div = Gtk.Button(_("Division"))
        self.div.show()
        h2.add(self.div)

        cont.add(h1)
        cont.add(h2)
        oper.add(cont)

        self.agregar.add(oper)
        self.agregar.add(herr)

    def setDeshacerListeners(self, functions):
        for f in functions:
            self.undo.connect("button_press_event", f)

    def setHistListeners(self, functions):
        for f in functions:
            self.adj.connect("value_changed", f)

    def setGuardarListeners(self, functions):
         for f in functions:
            self.keep.connect("button_press_event", f)

    def setAbrirListeners(self, functions):
        for f in functions:
            self.open.connect("button_press_event", f)

    def setSumaListeners(self, functions):
        for f in functions:
            self.suma.connect("button_press_event", f)

    def setRestaListeners(self, functions):
        for f in functions:
            self.resta.connect("button_press_event", f)

    def setMultiplicacionListeners(self, functions):
        for f in functions:
            self.mult.connect("button_press_event", f)

    def setDivisionListeners(self, functions):
        for f in functions:
            self.div.connect("button_press_event", f)

    def setZoomListeners(self, functions):
        for f in functions:
            self.adj2.connect("value_changed", f)

    def setBorrarListeners(self, functions):        
        self.borrarListeners = functions

    def __clicBorrar(self, object, data):
        for f in self.borrarListeners:
            f(-1)


    def cargarAdj(self, value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0):
        #Gtk.Adjustment(value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0)
        if self.adj!=None:
            del self.adj
        if self.history !=None:
            self.cont2.remove(self.history)
            del self.history

        self.adj =  Gtk.Adjustment(value, lower, upper, step_incr, page_incr, page_size)
        self.history = Gtk.HScale.new(self.adj)
        self.history.set_digits(0)
        self.history.show()
        self.cont2.add(self.history)
