class Imc:
    def __init__(self, massa, altura):
        self.massa = massa
        self.altura = altura
    
    def calcularImc(massa, altura):
        resulImc = massa / (altura ** 2)
        print('=========================\nIMC:', round(resulImc,2))

class Rcq:
    def __init__(self, circunCintura, circunQuadril):
        self.cincunCintura = circunCintura
        self.circunQuadril = circunQuadril

    def calcularRcq(circunCintura, circunQuadril):
        resulRcq = circunCintura / circunQuadril
        print('=========================\nRCQ:', round(resulRcq,2))

class Iac:
    def __init__(self, circunQuadril, altura):
        self.circunQuadril = circunQuadril
        self.altura = altura

    def calcularIac(circunQuadril, altura):
        resulIac = (circunQuadril / (altura * (altura**0.5))) - 18
        print('=========================\nIAC:', round(resulIac,2))
