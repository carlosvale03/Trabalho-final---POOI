class SocioTorcedor:
    def __init__(self, nome, cpf, valor):
        self._socio = nome
        self._cpf = cpf
        self._valor = valor

    @property
    def socio(self):
        return self._socio

    @property
    def cpf(self):
        return self._cpf

    @property
    def valor(self):
        return self._valor

    def arrecada(self):
        return self._valor