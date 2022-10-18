from arrecadacao import Iarrecadacao

class Dicionarios:
    def __init__(self):
        self._jogos = dict()
        self._ingresso = dict()
        self._setorA = dict()
        self._setorB = dict()
        self._setorC = dict()
        self._camarote = dict()
        self._socios = dict()


    @property
    def jogos(self):
        return self._jogos

    @property
    def ingressos(self):
        return self._ingresso

    @property
    def setorA(self):
        return self._setorA

    @property
    def setorB(self):
        return self._setorB

    @property
    def setorC(self):
        return self._setorC

    @property
    def camarote(self):
        return self._camarote

    @property
    def socios(self):
        return self._socios

    def calcular_arrecadacao(self):
        sist = SistemaArrecadacao()
        arrecadacao = 0
        for objeto in self._setorA.values():
            lista = sist.Arrecadador(objeto)
            arrecadacao += sum(lista)
        
        for objeto in self._setorB.values():
            lista = sist.Arrecadador(objeto) 
            arrecadacao += sum(lista)

        for objeto in self._setorC.values():
            lista = sist.Arrecadador(objeto)
            arrecadacao += sum(lista)

        for objeto in self._camarote.values():
            lista = sist.Arrecadador(objeto)
            arrecadacao += sum(lista)

        for objeto in self._socios.values():
            arrecadacao += sist.Arrecadador(objeto)

        return arrecadacao
        


class SistemaArrecadacao:
    def Arrecadador(self, obj):
        if isinstance(obj, Iarrecadacao):
            return obj.arrecada()