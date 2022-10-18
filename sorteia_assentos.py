from random import randint


# lista de assentos de cada setor
Assentos_setorA = dict()
Assentos_setorB = dict()
Assentos_setorC = dict()
Assentos_camarote = dict()

setorA = list()
setorB = list()
setorC = list()
camarote = list()

# função para sortear números das contas


def sorteia_setorA(capacidade, id_partida):
    num = randint(1, capacidade+1)

    # condicional para impedir que 2 numeros iguais sejam sorteados
    if num in Assentos_setorA.keys():
        sorteia_setorA(capacidade, id_partida)
    else:
        setorA.append(num)
        Assentos_setorA[id_partida] = setorA
        return num



def sorteia_setorB(capacidade, id_partida):
    num = randint(1, capacidade+1)

    # condicional para impedir que 2 numeros iguais sejam sorteados
    if num in Assentos_setorB.keys():
        sorteia_setorB(capacidade, id_partida)
    else:
        setorB.append(num)
        Assentos_setorB[id_partida] = setorB
        return num



def sorteia_setorC(capacidade, id_partida):
    num = randint(1, capacidade+1)

    # condicional para impedir que 2 numeros iguais sejam sorteados
    if num in Assentos_setorC.keys():
        sorteia_setorC(capacidade, id_partida)
    else:
        setorC.append(num)
        Assentos_setorC[id_partida] = setorC
        return num



def sorteia_camarote(capacidade, id_partida):
    num = randint(1, capacidade+1)

    # condicional para impedir que 2 numeros iguais sejam sorteados
    if num in Assentos_camarote.keys():
        sorteia_camarote(capacidade, id_partida)
    else:
        setorA.append(num)
        Assentos_camarote[id_partida] = camarote
        return num