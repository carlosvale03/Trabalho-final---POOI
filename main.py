from random import randint
from estadio import Iestadio, SetorA, SetorB, SetorC, Camarote
from dicionarios import Dicionarios
from jogo import Jogos
from arrecadacao import Iarrecadacao
from socio_torcedor import SocioTorcedor
import datefinder
dicio = Dicionarios()
capacidade_total = 1000
setorA = SetorA('', '', capacidade_total)
setorB = SetorB('', '', capacidade_total)
setorC = SetorC('', '', capacidade_total)
camarote = Camarote('', '', capacidade_total)

Iarrecadacao.register(Iestadio)
Iarrecadacao.register(SocioTorcedor)


def menu():
    print()
    print('=-' * 7, ' SELECIONE UMA OPÇÃO ', '-=' * 7)
    print(''' 1 - CADASTRA JOGO \n 2 - COMPRAR INGRESSO \n 3 - IMPRIMIR INGRESSOS DE UMA PESSOA \n 4 - CONFERIR HORÁRIOS DE JOGOS
 5 - CADASTRAR SÓCIO TORCEDOR \n 6 - CONFERIR QUANTIDADE DE INGRESSOS VENDIDOS \n 7 - IMPRIMIR CADEIRAS DISPONIVEIS NOS SETORES
 8 - CALCULAR ARRECADAÇÃO \n 9 - ENCERRAR O PROGRAMA''')
    print('=-' * 26)


def menu_local():
    print()
    print('=-' * 4, ' ESCOLHA UMA REGIÃO DO ESTADIO ', '-=' * 4)
    print('1 - Setor A \n2 - Setor B \n3 - Setor C \n4 - Camarote')
    print('=-' * 16)


def menu_local_valor(tipo):
    print()
    print('=-' * 4, ' ESCOLHA UMA REGIÃO DO ESTADIO ', '-=' * 4)
    print(tipo)
    print('1 - Setor A R$50,00 \n2 - Setor B R$65,00 \n3 - Setor C R$80,00 \n4 - Camarote R$150,00')
    print('=-' * 16)


def menu_local_valor_socio(tipo):
    print()
    print('=-' * 4, ' ESCOLHA UMA REGIÃO DO ESTADIO ', '-=' * 4)
    print(tipo)
    print('1 - Setor A R$25,00 \n2 - Setor B R$32,50 \n3 - Setor C R$40,00 \n4 - Camarote R$75,00')
    print('=-' * 16)


def proximos_jogos():
    print('PROXIMOS JOGOS: ')
    for i in dicio.jogos:
        print('=='*20)
        print(f'Campeonato: {dicio.jogos[i].campeonato}')
        print(
            f'{dicio.jogos[i].time_casa} x {dicio.jogos[i].time_visitante}')
        strData = dicio.jogos[i].data_hora.strftime(
            "DATA: %d/%m/%Y - HORA: %H:%M")
        print(strData)
        print(f'id do jogo: {i}')
        print('=='*20)


# lista para armazenar cpfs
cpfs = list()


def confereCpf(chave):
    if chave in cpfs:
        return False
    else:
        cpfs.append(chave)
        return True


# lista para armazenar ids de jogos
idJogos = list()
idJogos.append(1000)
idJogos.append(1001)

# função para gerar ids para jogos


def id_jogos():
    IdJogo = randint(1000, 10000)
    if IdJogo in idJogos:
        id_jogos()
    else:
        idJogos.append(IdJogo)
        return IdJogo


if __name__ == '__main__':
    # jogos ja cadastrados para facilitar o processo do codigo
    # =-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    dt_str = '22/10/2022 19:00'
    dt_objeto = datefinder.find_dates(dt_str)
    for d in dt_objeto:
        dt = d
    dicio.jogos[1000] = Jogos(
        dt, 'Santos', 'Corinthias', 'Brasileiro')

    dt_str = '11/05/2022 16:30'
    dt_objeto = datefinder.find_dates(dt_str)
    for d in dt_objeto:
        dt = d
    dicio.jogos[1001] = Jogos(
        dt, 'Santos', 'Avaí', 'Brasileiro')
    # =-=-=-=--=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-

    while True:
        menu()
        try:
            op = int(input('Opção: '))
            assert 1 <= op <= 9
            print()

            if op == 1:
                print('=-' * 7, 'CADASTRAR JOGO', '-=' * 7)
                while True:
                    # Para a data vai ser recebido um texto com a data do jogo
                    dia = input(
                        "Digite a data do jogo (dd/mm/aaaa): ")
                    hora = input('Digite o horario do jogo (hh:mm): ')
                    data_hora = dia + ' ' + hora
                    # Esse texto será processado com o find_dates do datefinder  com source = True para retornar o valor igual o que foi digitado
                    data = datefinder.find_dates(data_hora)
                    # para o valor ser retornado no mesmo formato que foi digitado ( dd/mm/aa )
                    for d in data:
                        dt_jogo = d

                    # conferir se a variavel foi declarada
                    if 'dt_jogo' in locals():
                        break
                    else:
                        print('Formato invalido!\n')

                time_casa = input('Digite o nome do time mandante: ')
                time_visitante = input('Digite o nome do time visitante: ')
                campeonato = input('Digite o nome do campeonato deste jogo: ')

                idJogo = id_jogos()
                dicio.jogos[idJogo] = Jogos(
                    dt_jogo, time_casa, time_visitante, campeonato)

                print(
                    f'Jogo entre {time_casa} e {time_visitante} será realizado em {dt_jogo}!')

            if op == 2:
                print('=-' * 7, 'COMPRAR INGRESSO', '-=' * 7)
                proximos_jogos()

                jogo_id = int(input('Digite o id do jogo desejado: '))
                nome = input('Digite seu nome: ')
                cpf = input('Digite seu cpf: ')

                jogo = f'{dicio.jogos[jogo_id].time_casa} X {dicio.jogos[jogo_id].time_visitante}'
                hora = dicio.jogos[jogo_id].data_hora
                socios = dicio.socios
                if cpf in socios:
                    tipo_ingresso = 'Ingresso para sócio torcedor'
                else:
                    tipo_ingresso = 'Ingresso normal'

                while True:
                    if tipo_ingresso == 'Ingresso para sócio torcedor':
                        menu_local_valor_socio(tipo_ingresso)
                    else:
                        menu_local_valor(tipo_ingresso)
                    try:
                        op_local = int(input('Opção: '))
                        assert 1 <= op_local <= 4
                        break
                    except ValueError:
                        print('Valor invalido! :(')
                    except AssertionError:
                        print('Opção invalida! :(')

                if op_local == 1:
                    if cpf not in dicio.setorA:
                        dicio.setorA[cpf] = SetorA(
                            nome, cpf,  capacidade_total)
                    valor = 50.0
                    compra = dicio.setorA[cpf].compra_ingresso(
                        valor, jogo, socios, hora, jogo_id)
                elif op_local == 2:
                    if cpf not in dicio.setorB:
                        dicio.setorB[cpf] = SetorB(nome, cpf, capacidade_total)
                    valor = 65.0
                    compra = dicio.setorB[cpf].compra_ingresso(
                        valor, jogo, socios, hora, jogo_id)
                elif op_local == 3:
                    if cpf not in dicio.setorC:
                        dicio.setorC[cpf] = SetorC(nome, cpf, capacidade_total)
                    valor = 80.0
                    compra = dicio.setorC[cpf].compra_ingresso(
                        valor, jogo, socios, hora, jogo_id)
                elif op_local == 4:
                    if cpf not in dicio.camarote:
                        dicio.camarote[cpf] = Camarote(
                            nome, cpf, capacidade_total)
                    valor = 150.0
                    compra = dicio.camarote[cpf].compra_ingresso(
                        valor, jogo, socios, hora, jogo_id)

                if compra == True:
                    print('Ingresso comprado!')
                else:
                    print('Falha')

            elif op == 3:
                print('=-' * 7, 'IMPRIMIR INGRESSOS DE UMA PESSOA', '-=' * 7)
                cpf = input('Digite o CPF do torcedor: ')
                confere = confereCpf(cpf)
                if confere == True:
                    if cpf in dicio.setorA:
                        dicio.setorA[cpf].imprime_ingresso(cpf)
                        print()
                    elif cpf in dicio.setorB:
                        dicio.setorB[cpf].imprime_ingresso(cpf)
                        print()
                    elif cpf in dicio.setorC:
                        dicio.setorC[cpf].imprime_ingresso(cpf)
                        print()
                    elif cpf in dicio.camarote:
                        dicio.camarote[cpf].imprime_ingresso(cpf)
                        print()
                    else:
                        print(
                            'A pessoa com o CPF informado ainda não possuí ingressos.')

                # imprime_ingresso(cpf)

            elif op == 4:
                print('=-' * 7, 'CONFERIR HORÁRIOS DE JOGOS', '-=' * 7)
                proximos_jogos()

            elif op == 5:
                print('=-' * 7, 'CADASTRAR SÓCIO TORCEDOR', '-=' * 7)
                valor_socio = 25.00
                print(
                    'QUANDO VOCÊ É SÓCIO TORCEDOR VOCÊ AJUDA SEU TIME A CRESCER E AINDA GARANTE VANTAGENS')
                print(
                    f'Para ser sócio torcedor você terá que pagar uma taxa de apenas R${valor_socio}\n')
                while True:
                    try:
                        cond = int(input(
                            'Para se cadastrar como sócio torcedor digite 1, para cancelar digite 2: '))
                        assert 1 <= cond <= 2
                        break
                    except ValueError:
                        print('Valor invalido! :(')
                    except AssertionError:
                        print('Opção invalida! :(')
                if cond == 1:
                    nome = input('\nDigite seu nome: ')
                    cpf = input('Digite o CPF: ')
                    if cpf in dicio.socios:
                        print('O CPF informado já está cadastrado como sócio torcedor')
                    else:
                        dicio.socios[cpf] = SocioTorcedor(nome, cpf, valor_socio)
                        print(
                            f'\nParabéns {nome}, você agora é um sócio torcedor!')
                else:
                    print('Continue pagando mais caro no ingresso :)')

            elif op == 6:
                print('=-' * 7, 'QUANTIDADE DE INGRESSOS VENDIDOS', '-=' * 7)
                vendidos = setorA.cont_setorA + setorB.cont_setorB + \
                    setorC.cont_setorC + camarote.cont_camarote
                if vendidos == 0:
                    print('Até o momento não foram vendidos ingressos')
                elif vendidos == 1:
                    print(
                        f'Até o momento foi vendido apenas {vendidos} ingresso')
                else:
                    print(f'Até o momento foram vendidos {vendidos} ingressos')

            elif op == 7:
                print('=-' * 7, 'CADEIRAS DISPONIVEIS NOS SETORES', '-=' * 7)
                proximos_jogos()
                id_partida = int(input('Digite o id da partida: '))
                menu_local()

                while True:
                    try:
                        op = int(input('Opção: '))
                        assert 1 <= op <= 4
                        break

                    except ValueError:
                        print('Valor invalido! :(')
                    except AssertionError:
                        print('Opção invalida! :(')

                if op == 1:
                    setorA.imprime_assentos(id_partida)
                elif op == 2:
                    setorB.imprime_assentos(id_partida)
                elif op == 3:
                    setorC.imprime_assentos(id_partida)
                elif op == 4:
                    camarote.imprime_assentos(id_partida)

            elif op == 8:
                print('=-' * 7, 'CALCULO DA ARRECADAÇÃO', '-=' * 7)
                arrecadacao = 0
                arrecadacao = dicio.calcular_arrecadacao()
                print(f'Foram arrecadados R${arrecadacao} até o momento')

            elif op == 9:
                print('PROGRAMA ENCERRADO')
                break

        except ValueError:
            print('Valor invalido! :(')
        except AssertionError:
            print('Opção invalida! :(')
