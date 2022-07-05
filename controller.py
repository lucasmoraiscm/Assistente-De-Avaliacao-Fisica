from model import *

class ImcController():
    @classmethod
    def calcularImcController(cls, massa, altura): #Recebe os dados vindos da view
        if massa > 0 and altura > 0: #Tratamento dos dados
            imc1 = Imc(massa, altura) #Montando o objeto
            Imc.calcularImc(imc1.massa, imc1.altura) #Solicitação de cálculo na model
        else:
            print('=========================\nAção inválida!') #Tratamento de erro

class RcqController():
    @classmethod
    def calcularRcqController(cls, circunCintura, circunQuadril): #Recebe os dados vindos da view
        if circunCintura > 0 and circunQuadril > 0: #Tratamento dos dados
            rcq1 = Rcq(circunCintura, circunQuadril) #Montando o objeto
            Rcq.calcularRcq(rcq1.cincunCintura, rcq1.circunQuadril) #Solicitação de cálculo na model
        else:
            print('=========================\nAção inválida!') #Tratamento de erro

class IacController():
    @classmethod
    def calcularIacController(cls, circunQuadril, altura): #Recebe os dados vindos da view
        if circunQuadril > 0 and altura > 0: #Tratamento dos dados
            iac1 = Iac(circunQuadril, altura) #Montando o objeto
            Iac.calcularIac(iac1.circunQuadril, iac1.altura) #Solicitação de cálculo na model
        else:
            print('=========================\nAção inválida!') #Tratamento de erro
