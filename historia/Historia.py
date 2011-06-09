__author__="rodripf"
__date__ ="$17/05/2011 10:43:58 AM$"

from Suceso import Suceso

class Historia:
    def __init__(self):
        self.suc = []
        self.actual = 0

        dummy = Suceso(-1)
        self.suc.append(dummy)

    def agregar(self, suceso):
        if self.actual < len(self.suc) - 1:
            for i in xrange(self.actual+1, len(self.suc)): #borro todos los posteriores al actual nuevo
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
            if tipo == 0:
                valores = nuevo.getValor()
                obj = nuevo.getObjeto()
                operacion.setValor(obj[0], obj[1], valores[1])
            elif tipo == 1:
                operacion.factores.agregarUno()
            elif tipo==2:
                operacion.factores.quitarUno()
            elif tipo == 3:
                obj = nuevo.getObjeto()
                operacion.factores.factores[obj].digitos.agregarUno()
            elif tipo == 4:
                obj = nuevo.getObjeto()
                operacion.factores.factores[obj].digitos.quitarUno()

        elif self.actual > lugar: #me muevo hacia la izquierda
            if self.actual - lugar > 1:
                self.setPosicion(lugar+1, operacion)

            actual = self.suc[self.actual]
            tipo = actual.getTipo()
            if  tipo == 0:
                valores = actual.getValor()
                obj = actual.getObjeto()
                operacion.setValor(obj[0], obj[1], valores[0])
            elif tipo == 1:
                operacion.factores.quitarUno()
            elif tipo == 2:
                operacion.factores.agregarUno()
            elif tipo == 3:
                obj = actual.getObjeto()
                operacion.factores.factores[obj].digitos.quitarUno()
            elif tipo == 4:
                obj = actual.getObjeto()
                operacion.factores.factores[obj].digitos.agregarUno()

        self.actual = lugar