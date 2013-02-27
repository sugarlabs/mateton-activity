__author__="rodripf"
__date__ ="$17/05/2011 10:32:17 AM$"

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

class Suceso:
    #tipo: 0->cambio de valor, 1->agrego factor a factores, 2-> quito factor de factores
    #       3->agrego digitos a factor, 4->quito digitos a factor
    def __init__(self, tipo):
        self.tipo = tipo

    def setObjeto(self, idFactor, idDigito = -1):
        self.idFactor = idFactor
        self.idDigito = idDigito

    def setValor(self, valor):
        self.valor = valor #de la forma (anterior, actual)

    def getObjeto(self):
        if self.tipo == 0:
            return (self.idFactor, self.idDigito)
        elif self.tipo == 3 or self.tipo == 4:
            return self.idFactor

    def getValor(self):
        if self.tipo == 0:
            return self.valor
        else:
            return None

    def getTipo(self):
        return self.tipo

    def igualA(self, suc):
        if suc.getTipo() == self.getTipo():
            if suc.getTipo() == 0:
                if self.getObjeto() == suc.getObjeto():
                    return True
                else:
                    return False
        else:
            return False
