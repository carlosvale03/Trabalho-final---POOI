# sorteia_setorA, sorteia_setorB, sorteia_setorC, sorteia_camarote
from sorteia_assentos import sorteia_setorA, sorteia_setorB, sorteia_setorC, sorteia_camarote, Assentos_camarote
from imprime_assentos import imprime_assentos_setorA, imprime_assentos_setorB, imprime_assentos_setorC
import datetime
import abc
from dicionarios import Dicionarios
dicio = Dicionarios()


# interface
class Iestadio(abc.ABC):
    def __init__(self, capacidade_total=1000):
        self._capac_total = capacidade_total

    @property
    def capacidade_total(self):
        return self._capac_total

    @capacidade_total.setter
    def capacidade_total(self, capacidade_total):
        self.capacidade_total = capacidade_total

    @abc.abstractmethod
    def compra_ingresso(self, valor, jogo, socios, horario, id_partida):
        '''Essa é uma função abstrata para efetuar a compra do ingresso.
        Essa função vai receber como parametro o valor pago e o tipo de pagamento.
        Essa função vai retornar True se o ingresso for vendido ou False
        se ele não for vendido.'''

    @abc.abstractmethod
    def imprime_ingresso(self, cpf):
        '''Essa é uma função abstrata para imprimir os ingressos de uma pessoa.'''

    @abc.abstractmethod
    def imprime_assentos(self, id_partida):
        '''Essa é uma função abstrata para imprimir os assentos disponiveis da regiao escolhida no estadio.'''
 
    def desconto(self):
        '''Essa é uma função abstrata para calcular o desconto para socio torcedores'''

    @abc.abstractmethod
    def arrecada(self):
        '''Método abstrato para arrecadar os valores.
        Esse método vai retornar cada valor arrecadado.'''


class SetorA(Iestadio):
    cont_setorA = 0

    def __init__(self, nome, cpf, capacidade_total=1000):
        super().__init__(capacidade_total)
        self._torcedor = nome
        self._cpf = cpf
        self._setor = 'Setor A'
        self._valor = 50.0
        self.arrecadadorA = list()

    @property
    def setor(self):
        return self._setor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def set_valor(self, valor):
        self._valor = valor

    @property
    def torcedor(self):
        return self._torcedor

    @property
    def cpf(self):
        return self._cpf

    def arrecada(self):
        return self.arrecadadorA

    def desconto(self):
        self._valor = self._valor/2

    def compra_ingresso(self, valor, jogo, socios, horario, id_partida):
        capacidade_setor = int(self._capac_total/2.5)
        if capacidade_setor >= SetorA.cont_setorA:
            SetorA.cont_setorA += 1
            if self._cpf in socios:
                valor = valor/2
                SetorA.desconto(self)
                tipo_torcedor = 'Sócio'
            else:
                tipo_torcedor = 'Normal'

            if self._valor <= valor:
                assento = sorteia_setorA(capacidade_setor, id_partida)
                data = datetime.datetime.now()
                data_hora_compra = data.strftime(
                    "DATA DA COMPRA: %d/%m/%Y - HORA: %H:%M")
                data_jogo = horario.strftime(
                    "DATA DO JOGO: %d/%m/%Y - HORA: %H:%M")
                ingresso = [['=='*27], ['VISTA A CAMISA DO SEU TIME E VENHA COMEMORAR COMIGO!'], [jogo], [
                    'INGRESSO PARA O SETOR A'], [f'{self._torcedor}'], [f'Assento n°: {assento}'], [f'TIPO DE INGRESSO: {tipo_torcedor} - VALOR: R${self._valor}'], [
                        data_hora_compra], ['Local: Estadio Josefino Vieira'], [data_jogo], ['=='*27]]
                if self._cpf in dicio.ingressos:
                    dicio.ingressos[self._cpf] += ingresso
                else:
                    dicio.ingressos[self._cpf] = ingresso

                self.arrecadadorA.append(self._valor)
                return True
            else:
                return False

    def imprime_ingresso(self, cpf):
        for i in dicio.ingressos[cpf]:
            print(*i)

    def imprime_assentos(self, id_partida):
        capacidade_setor = int(self._capac_total/2.5)
        imprime_assentos_setorA(capacidade_setor, id_partida)


class SetorB(Iestadio):
    cont_setorB = 0

    def __init__(self, nome, cpf,  capacidade_total=1000):
        super().__init__(capacidade_total)
        self._torcedor = nome
        self._cpf = cpf
        self._setor = 'Setor B'
        self._valor = 65.0
        self.arrecadadorB = list()

    @property
    def setor(self):
        return self._setor

    @property
    def valor(self):
        return self._valor

    @property
    def torcedor(self):
        return self._torcedor

    @property
    def cpf(self):
        return self._cpf

    def arrecada(self):
        return self.arrecadadorB

    def desconto(self):
        self._valor = self._valor/2

    def compra_ingresso(self, valor, jogo, socios, horario, id_partida):
        capacidade_setor = int(self._capac_total/3.33)
        if capacidade_setor >= SetorB.cont_setorB:
            SetorB.cont_setorB += 1

            if self._cpf in socios:
                valor = valor/2
                SetorB.desconto(self)
                tipo_torcedor = 'Sócio'
            else:
                tipo_torcedor = 'Normal'

            if self._valor <= valor:
                assento = sorteia_setorB(capacidade_setor, id_partida)
                data = datetime.datetime.now()
                data_hora_compra = data.strftime(
                    "DATA DA COMPRA: %d/%m/%Y - HORA: %H:%M")
                data_jogo = horario.strftime(
                    "DATA DO JOGO: %d/%m/%Y - HORA: %H:%M")
                ingresso = [['=='*27], ['VISTA A CAMISA DO SEU TIME E VENHA COMEMORAR COMIGO!'], [jogo], [
                    'INGRESSO PARA O SETOR B'], [f'{self._torcedor}'], [f'Assento n°: {assento}'], [f'TIPO DE INGRESSO: {tipo_torcedor} - VALOR: R${self._valor}'], [
                        data_hora_compra], ['Local: Estadio Josefino Vieira'], [data_jogo], ['=='*27]]
                if self._cpf in dicio.ingressos:
                    dicio.ingressos[self._cpf] += ingresso
                else:
                    dicio.ingressos[self._cpf] = ingresso

                self.arrecadadorB.append(self._valor)
                return True
            else:
                return False

    def imprime_ingresso(self, cpf):
        for i in dicio.ingressos[cpf]:
            print(*i)

    def imprime_assentos(self, id_partida):
        capacidade_setor = int(self._capac_total/3.33)
        imprime_assentos_setorB(capacidade_setor, id_partida)


class SetorC(Iestadio):
    cont_setorC = 0

    def __init__(self, nome, cpf,  capacidade_total=1000):
        super().__init__(capacidade_total)
        self._torcedor = nome
        self._cpf = cpf
        self._setor = 'Setor C'
        self._valor = 80.0
        self.arrecadadorC = list()

    @property
    def setor(self):
        return self._setor

    @property
    def valor(self):
        return self._valor

    @property
    def torcedor(self):
        return self._torcedor

    @property
    def cpf(self):
        return self._cpf

    def arrecada(self):
        return self.arrecadadorC

    def desconto(self):
        self._valor = self._valor/2

    def compra_ingresso(self, valor, jogo, socios, horario, id_partida):
        capacidade_setor = int(self._capac_total/5)
        if capacidade_setor >= SetorC.cont_setorC:
            SetorC.cont_setorC += 1

            if self._cpf in socios:
                valor = valor/2
                SetorC.desconto(self)
                tipo_torcedor = 'Sócio'
            else:
                tipo_torcedor = 'Normal'

            if self._valor <= valor:
                assento = sorteia_setorC(capacidade_setor, id_partida)
                data = datetime.datetime.now()
                data_hora_compra = data.strftime(
                    "DATA DA COMPRA: %d/%m/%Y - HORA: %H:%M")
                data_jogo = horario.strftime(
                    "DATA DO JOGO: %d/%m/%Y - HORA: %H:%M")
                ingresso = [['=='*27], ['VISTA A CAMISA DO SEU TIME E VENHA COMEMORAR COMIGO!'], [jogo], [
                    'INGRESSO PARA O SETOR C'], [f'{self._torcedor}'], [f'Assento n°: {assento}'], [f'TIPO DE INGRESSO: {tipo_torcedor} - VALOR: R${self._valor}'], [
                        data_hora_compra], ['Local: Estadio Josefino Vieira'], [data_jogo], ['=='*27]]
                if self._cpf in dicio.ingressos:
                    dicio.ingressos[self._cpf] += ingresso
                else:
                    dicio.ingressos[self._cpf] = ingresso

                self.arrecadadorC.append(self._valor)
                return True
            else:
                return False

    def imprime_ingresso(self, cpf):
        for i in dicio.ingressos[cpf]:
            print(*i)

    def imprime_assentos(self, id_partida):
        capacidade_setor = int(self._capac_total/5)
        imprime_assentos_setorC(capacidade_setor, id_partida)


class Camarote(Iestadio):
    cont_camarote = 0

    def __init__(self, nome, cpf,  capacidade_total=1000):
        super().__init__(capacidade_total)
        self._torcedor = nome
        self._cpf = cpf
        self._setor = 'Camarote'
        self._valor = 150.0
        self.arrecadadorCamarote = list()

    @property
    def setor(self):
        return self._setor

    @property
    def valor(self):
        return self._valor

    @property
    def torcedor(self):
        return self._torcedor

    @property
    def cpf(self):
        return self._cpf

    def arrecada(self):
        return self.arrecadadorCamarote

    def desconto(self):
        self._valor = self._valor/2

    def compra_ingresso(self, valor, jogo, socios, horario, id_partida):
        capacidade_setor = int(self._capac_total/10)
        if capacidade_setor >= Camarote.cont_camarote:
            Camarote.cont_camarote += 1

            if self._cpf in socios:
                tipo_torcedor = 'Sócio'
                valor = valor/2
                Camarote.desconto(self)
            else:
                tipo_torcedor = 'Normal'

            if self._valor <= valor:
                assento = sorteia_camarote(capacidade_setor, id_partida)
                data = datetime.datetime.now()
                data_hora_compra = data.strftime(
                    "DATA DA COMPRA: %d/%m/%Y - HORA: %H:%M")
                data_jogo = horario.strftime(
                    "DATA DO JOGO: %d/%m/%Y - HORA: %H:%M")
                ingresso = [['=='*27], ['VISTA A CAMISA DO SEU TIME E VENHA COMEMORAR COMIGO!'], [jogo], [
                    'INGRESSO PARA O SETOR CAMAROTE'], [f'{self._torcedor}'], [f'Assento n°: {assento}'], [f'TIPO DE INGRESSO: {tipo_torcedor} - VALOR: R${self._valor}'], [
                        data_hora_compra], ['Local: Estadio Josefino Vieira'], [data_jogo], ['=='*27]]
                if self._cpf in dicio.ingressos:
                    dicio.ingressos[self._cpf] += ingresso
                else:
                    dicio.ingressos[self._cpf] = ingresso

                self.arrecadadorCamarote.append(self._valor)
                return True
            else:
                return False

    def imprime_ingresso(self, cpf):
        for i in dicio.ingressos[cpf]:
            print(*i)

    def imprime_assentos(self, id_partida):
        capacidade_setor = int(self._capac_total/10)
        if id_partida in Assentos_camarote:
            Assentos_camarote[id_partida].sort()
            cont = 0
            for i in range(1, capacidade_setor+1):

                if cont == int(capacidade_setor/4):
                    print()
                    cont = 0
                if i in Assentos_camarote[id_partida]:
                    print('   ', end=' ')
                else:
                    if i < 10:
                        print('00' + str(i), end=' ')
                    elif i < 100:
                        print('0' + str(i), end=' ')
                    else:
                        print(str(i), end=' ')
                    cont += 1
        else:
            cont = 0
            for i in range(1, capacidade_setor+1):

                if cont == int(capacidade_setor/4):
                    print()
                    cont = 0
                if i < 10:
                    print('00' + str(i), end=' ')
                elif i < 100:
                    print('0' + str(i), end=' ')
                else:
                    print(str(i), end=' ')
                cont += 1
