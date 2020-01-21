__author__="rodripf"
__date__ ="$20/05/2011 12:12:20 PM$"

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
from sugar3.activity import activity
import pickle
from Suma import Suma
from Resta import Resta
from Multiplicacion import Multiplicacion
from Division import Division
import os

class Manager:
    def __init__(self, funcDigit):
        self.funcionesDigitos = funcDigit

    def setHistoria(self, hist):
        self.historia = hist

    def setEstadoOperacion(self, oper):
        self.operacion = oper

    def guardar(self):
        actRoot = activity.get_activity_root()
        saveFolder = actRoot + "/data/saves/"
        
        if not os.path.exists(saveFolder):
            os.makedirs(saveFolder)
        
        saveFile = saveFolder + self.archivo        

        file1 = open(saveFile + ".hst", "wb")
        pikH = pickle.Pickler(file1)
        pikH.dump(self.historia)


        file2 = open(saveFile + ".opr", "wb")
        pikO = pickle.Pickler(file2)
        pikO.dump(self.operacion)

    def abrir(self):
        actRoot = activity.get_activity_root()
        saveFolder = actRoot + "/data/saves/"
        saveFile = saveFolder + self.archivo

        file1 = open(saveFile + ".hst", "rb")
        pikH = pickle.Unpickler(file1)
        historia = pikH.load()

        file2 = open(saveFile + ".opr", "rb")
        pikO = pickle.Unpickler(file2)
        eo = pikO.load()

        if eo.tipo == 0:
            operacion = Suma(self.funcionesDigitos)
        elif eo.tipo == 1:
            operacion = Resta(self.funcionesDigitos)
        elif eo.tipo == 2:
            operacion = Multiplicacion(self.funcionesDigitos)
        elif eo.tipo == 3:
            operacion = Division(self.funcionesDigitos)

        historia.actual = 0
        for i in range(len(historia.suc)):
            historia.setPosicion(i, operacion)

        return (historia, operacion)
        

    def setArchivo(self, nombre):
        self.archivo = nombre

    def getArchivo(self):
        return self.archivo
