__author__="rodripf"
__date__ ="$23/05/2011 12:59:12 PM$"

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

class EstadoOperacion:
    def __init__(self, operacion):
        #0->suma, 1->resta, 2->multiplicacion, 3->division
        self.tipo = operacion.tipo

        self.cantFactores = len(operacion.factores.factores)
        self.cantDigitos = []
        self.valores = []

        for i in range(self.cantFactores):
            cantD = operacion.factores.factores[i].digitos.count
            self.cantDigitos.append(cantD)

            v = []
            for j in range(cantD):
                valor = operacion.factores.factores[i].digitos.digitos[j].getValor()
                v.append(valor)

            self.valores.append(v)

