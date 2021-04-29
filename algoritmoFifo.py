from sys import exit
import time

print("\n***************************** Algoritmo Fifo *****************************")

def adicionar():
    nome_processo = input('Digite o nome do seu processo ')
    lista_proc.append(nome_processo)
    tempo = float(input('Digite o tempo do seu processo '))
    lista_tempo.append(tempo)
    return lista_tempo

def mostrar():
        print('Lista de Processos: ',lista_proc,'\n')
        print('Lista do Tempo dos Processos: ',lista_tempo,'\n')

def sair():
    print('O programa sera encerrado...')
    exit(0)

def menu(numero_proc,cont=0):
    for i in range(numero_proc):
        while (cont < numero_proc):
            print("Selecione a operação desejada: \n")
            print("1 - Adicionar processo")
            print("2 - Mostrar processos")
            print("3 - Sair")
            escolha = int(input("Digite a opção 1/2/3 "))
            if (escolha == 1):
                cont = cont + 1
                adicionar()
            elif (escolha == 2 ):
                mostrar()
            elif (escolha == 3):
                sair()
            else:
                print('Vc selecionou uma opcao invalida. O programa sera encerrado...')
                sair()
            if (cont == numero_proc):
                print('Numero maximo de processos atingido')
                break

def mostrar_detalhes():
    for i in range(numero_proc - 1, 0, -1):
        lista_tempo_retorno.append(sum(lista_tempo[:-i]))
    lista_tempo_retorno.append(sum(lista_tempo))
    media_tempo_retorno = (sum(lista_tempo_retorno)) / numero_proc
    print('Tempo de Retorno dos Processos =', lista_tempo_retorno, '\n')
    print('Tempo Medio de Retorno dos Processos (TMR) =', round(media_tempo_retorno, 2), '\n')

    for i in range(numero_proc):
        lista_tempo_espera.append(sum(lista_tempo[:i]))
    media_tempo_espera = (sum(lista_tempo_espera)) / numero_proc
    print('Tempo de Espera dos Processos =', lista_tempo_espera, '\n')
    print('Tempo Medio de Espera dos Processos (TME) =', round(media_tempo_espera, 2), '\n')

    for i in range(numero_proc):
        lista_tr_te.append(lista_tempo_retorno[i] - lista_tempo_espera[i])
    print('Tempo de Processamento para Cada Processo =', lista_tr_te, '\n')
    tempo_proc_total = sum(lista_tr_te)
    print('Tempo Total de processamento =', tempo_proc_total, '\n')

escolha = 0
lista_proc = []
lista_tempo = []
lista_tempo_retorno = []
lista_tempo_espera = []
lista_tr_te = []
proc_total = 0
media_tempo_retorno = 0
media_tempo_espera = 0
cont = 0

numero_proc = int(input('Digite o numero de processos inseridos '))

menu(numero_proc)

mostrar()

print('Deseja visualizar detalhes de Tempo de Retorno e Tempo de Espera dos Processos?')
escolha = str(input('Digite s para sim ou n para nao '))
if (escolha == 's') or (escolha == 'S'):
    mostrar_detalhes()
    time.sleep(3)
    sair()
elif (escolha == 'n') or (escolha == 'N'):
    print('O programa nao exibira detalhes de TMR e TME')
    sair()
else:
    print('Vc nao selecionou uma opcao valida!!')
    sair()
