from controller import *

while True:
    try: 
        opc = int(input('=========================\n1-IMC\n2-RCQ\n3-IAC\n4-Sair\n=========================\nDigite a opção desejada: '))

        if opc == 1:
            massa = float(input('=========================\nDigite a massa: '))
            altura = float(input('Digite a altura: '))
            ImcController.calcularImcController(massa, altura)

        elif opc == 2:
            circunCintura = float(input('=========================\nDigite a circunferença da cintura: '))
            circunQuadril = float(input('Digite a circunferença do quadril: '))
            RcqController.calcularRcqController(circunCintura, circunQuadril)

        elif opc == 3:
            circunQuadril = float(input('=========================\nDigite a circunferença do quadril: '))
            altura = float(input('Digite a altura: '))
            IacController.calcularIacController(circunQuadril, altura)

        elif opc == 4:
            break

        else:
            print('=========================\nAção inválida!')

    except:
        print('=========================\nAção inválida!')
