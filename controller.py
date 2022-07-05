from model import *

class ImcController():
    @classmethod
    def calcularImcController(cls, massa, altura):
        if massa > 0 and altura > 0:
            imc1 = Imc(massa, altura)
            Imc.calcularImc(imc1.massa, imc1.altura)
        else:
            print('=========================\nAção inválida!')

class RcqController():
    @classmethod
    def calcularRcqController(cls, circunCintura, circunQuadril):
        if circunCintura > 0 and circunQuadril > 0:
            rcq1 = Rcq(circunCintura, circunQuadril)
            Rcq.calcularRcq(rcq1.cincunCintura, rcq1.circunQuadril)
        else:
            print('=========================\nAção inválida!')

class IacController():
    @classmethod
    def calcularIacController(cls, circunQuadril, altura):
        if circunQuadril > 0 and altura > 0:
            iac1 = Iac(circunQuadril, altura)
            Iac.calcularIac(iac1.circunQuadril, iac1.altura)
        else:
            print('=========================\nAção inválida!')
