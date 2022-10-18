from sorteia_assentos import Assentos_setorA, Assentos_setorB, Assentos_setorC


def imprime_assentos_setorA(capacidade_setor, id_partida):
    if id_partida in Assentos_setorA:
        Assentos_setorA[id_partida].sort()
        cont = 0
        for i in range(1, capacidade_setor+1):

            if cont == int(capacidade_setor/10):
                print()
                cont = 0
            if i in Assentos_setorA[id_partida]:
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

            if cont == int(capacidade_setor/10):
                print()
                cont = 0
            if i < 10:
                print('00' + str(i), end=' ')
            elif i < 100:
                print('0' + str(i), end=' ')
            else:
                print(str(i), end=' ')
            cont += 1


def imprime_assentos_setorB(capacidade_setor, id_partida):
    if id_partida in Assentos_setorB:
        Assentos_setorB[id_partida].sort()
        cont = 0
        for i in range(1, capacidade_setor+1):

            if cont == int(capacidade_setor/10):
                print()
                cont = 0
            if i in Assentos_setorB[id_partida]:
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

            if cont == int(capacidade_setor/10):
                print()
                cont = 0
            if i < 10:
                print('00' + str(i), end=' ')
            elif i < 100:
                print('0' + str(i), end=' ')
            else:
                print(str(i), end=' ')
            cont += 1


def imprime_assentos_setorC(capacidade_setor, id_partida):
    if id_partida in Assentos_setorC:
        Assentos_setorC[id_partida].sort()
        cont = 0
        for i in range(1, capacidade_setor+1):

            if cont == int(capacidade_setor/10):
                print()
                cont = 0
            if i in Assentos_setorC[id_partida]:
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

            if cont == int(capacidade_setor/10):
                print()
                cont = 0
            if i < 10:
                print('00' + str(i), end=' ')
            elif i < 100:
                print('0' + str(i), end=' ')
            else:
                print(str(i), end=' ')
            cont += 1
