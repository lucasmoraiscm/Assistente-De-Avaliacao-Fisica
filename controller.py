from model import *

class ImcController():
    @classmethod
    def calcularImcController(cls, massaImc, alturaImc): #Recebe os dados da view
            if massaImc > 0 and alturaImc > 0: #Tratamento dos dados
                imc1 = Imc(massaImc, alturaImc) #Montando o objeto
                respControllerImc = Imc.calcularImc(imc1.massa, imc1.altura) #Solicitação de cálculo na model
                return respControllerImc
            else:
                return 'Ação inválida!' #Tratamento de erro

class RcqController():
    @classmethod
    def calcularRcqController(cls, cincunCinturaRcq, circunQuadrilRcq): #Recebe os dados da view
            if cincunCinturaRcq > 0 and circunQuadrilRcq > 0: #Tratamento dos dados
                rcq1 = Rcq(cincunCinturaRcq, circunQuadrilRcq) #Montando o objeto
                respControllerRcq = Rcq.calcularRcq(rcq1.cincunCintura, rcq1.circunQuadril) #Solicitação de cálculo na model
                return respControllerRcq
            else:
                return 'Ação inválida!' #Tratamento de erro

class IacController():
    @classmethod
    def calcularIacController(cls, circunQuadrilIac, alturaIac): #Recebe os dados da view
            if circunQuadrilIac > 0 and alturaIac > 0: #Tratamento dos dados
                iac1 = Iac(circunQuadrilIac, alturaIac) #Montando o objeto
                respControllerIac = Iac.calcularIac(iac1.circunQuadril, iac1.altura) #Solicitação de cálculo na model
                return respControllerIac
            else:
                return 'Ação inválida!' #Tratamento de erro
