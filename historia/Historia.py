__author__="rodripf"
__date__ ="$17/05/2011 10:43:58 AM$"

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

from Suceso import Suceso

class Historia:
    def __init__(self):
        self.suc = []
        self.actual = 0

        dummy = Suceso(-1)
        self.suc.append(dummy)
        print(self.suc)

    def agregar(self, suceso):
        if self.actual < len(self.suc) - 1:
            for i in range(self.actual+1, len(self.suc)): #borro todos los posteriores al actual nuevo
                if len(self.suc) >= 1:
                    self.suc.pop()

        self.actual += 1
        self.suc.append(suceso)

    def getPosicion(self):
        return self.actual


    def setPosicion(self, lugar, operacion):
        if self.actual < lugar: #me muevo hacia la derecha
            if lugar - self.actual > 1:
                self.setPosicion(lugar - 1, operacion)

            nuevo = self.suc[lugar]
            tipo = nuevo.getTipo()
            if tipo == 0: #cambio valor
                valores = nuevo.getValor()
                obj = nuevo.getObjeto()
                operacion.setValor(obj[0], obj[1], valores[1])
            elif tipo == 1:
                if operacion.tipo != 2:
                    operacion.factores.agregarUno()
                else:
                    operacion.suma.factores.agregarUno()
                    operacion.factores.factores.append(operacion.suma.factores.factores[len(operacion.suma.factores.factores)-1])
            elif tipo==2:
                if operacion.tipo != 2:
                    operacion.factores.quitarUno()
                else:
                    operacion.suma.factores.quitarUno()
            elif tipo == 3:
                obj = nuevo.getObjeto()
                if obj >= 0:
                    operacion.factores.factores[obj].digitos.agregarUno()
                else:
                    operacion.extra[obj].digitos.agregarUno()
            elif tipo == 4:
                obj = nuevo.getObjeto()
                if obj >= 0:
                    operacion.factores.factores[obj].digitos.quitarUno()
                else:
                     operacion.extra[obj].digitos.quitarUno()

        elif self.actual > lugar: #me muevo hacia la izquierda
            if self.actual - lugar > 1 and (len(self.suc) >= self.actual) and (self.actual != 0):
                self.setPosicion(lugar+1, operacion)

            actual = self.suc[self.actual]
            tipo = actual.getTipo()
            if  tipo == 0:
                valores = actual.getValor()
                obj = actual.getObjeto()
                operacion.setValor(obj[0], obj[1], valores[0])
            elif tipo == 1:
                if operacion.tipo != 2:
                    operacion.factores.quitarUno()
                else:
                    operacion.suma.factores.quitarUno()
            elif tipo == 2:
                if operacion.tipo != 2:
                    operacion.factores.agregarUno()
                else:
                    operacion.suma.factores.quitarUno()
            elif tipo == 3:
                obj = actual.getObjeto()
                if obj >= 0:
                    operacion.factores.factores[obj].digitos.quitarUno()
                else:
                     operacion.extra[obj].digitos.quitarUno()
            elif tipo == 4:
                obj = actual.getObjeto()
                if obj >= 0:
                    operacion.factores.factores[obj].digitos.agregarUno()
                else:
                     operacion.extra[obj].digitos.agregarUno()

        self.actual = lugar
