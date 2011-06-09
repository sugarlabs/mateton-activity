__author__="rodripf"
__date__ ="$23/05/2011 12:59:12 PM$"

class EstadoOperacion:
    def __init__(self, operacion):
        #0->suma, 1->resta, 2->multiplicacion, 3->division
        self.tipo = operacion.tipo

        self.cantFactores = len(operacion.factores.factores)
        self.cantDigitos = []
        self.valores = []

        for i in xrange(self.cantFactores):
            cantD = operacion.factores.factores[i].digitos.count
            self.cantDigitos.append(cantD)

            v = []
            for j in xrange(cantD):
                valor = operacion.factores.factores[i].digitos.digitos[j].getValor()
                v.append(valor)

            self.valores.append(v)

