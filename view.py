from controller import *

while True:
    try: 
        #Menu de opções
        opc = int(input('=========================\n1-IMC\n2-RCQ\n3-IAC\n4-Sair\n=========================\nDigite a opção desejada: '))

        if opc == 1: #Opção IMC
            massa = float(input('=========================\nDigite a massa: '))
            altura = float(input('Digite a altura: '))
            ImcController.calcularImcController(massa, altura)

        elif opc == 2: #Opção RCQ
            circunCintura = float(input('=========================\nDigite a circunferença da cintura: '))
            circunQuadril = float(input('Digite a circunferença do quadril: '))
            RcqController.calcularRcqController(circunCintura, circunQuadril)

        elif opc == 3: #Opção IAC
            circunQuadril = float(input('=========================\nDigite a circunferença do quadril: '))
            altura = float(input('Digite a altura: '))
            IacController.calcularIacController(circunQuadril, altura)

        elif opc == 4: #Opção sair
            break

        else:
            print('=========================\nAção inválida!') #Tratamento de erro (número não presente no menu)

    except:
        print('=========================\nAção inválida!') #Tratamento de erro (dado que não é tipo int)
