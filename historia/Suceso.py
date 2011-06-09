__author__="rodripf"
__date__ ="$17/05/2011 10:32:17 AM$"

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