class Imc:
    def __init__(self, massa, altura): #Objeto IMC
        self.massa = massa
        self.altura = altura
    
    def calcularImc(massa, altura):
        resulImc = massa / (altura ** 2) #Cálculo do IMC
        print('=========================\nIMC:', round(resulImc,2)) #Resultado

class Rcq:
    def __init__(self, circunCintura, circunQuadril): #Objeto RCQ
        self.cincunCintura = circunCintura
        self.circunQuadril = circunQuadril

    def calcularRcq(circunCintura, circunQuadril): 
        resulRcq = circunCintura / circunQuadril #Cálculo do RCQ
        print('=========================\nRCQ:', round(resulRcq,2)) #Resultado

class Iac:
    def __init__(self, circunQuadril, altura): #Objeto IAC
        self.circunQuadril = circunQuadril
        self.altura = altura

    def calcularIac(circunQuadril, altura): 
        resulIac = (circunQuadril / (altura * (altura**0.5))) - 18 #Cálculo do IAC
        print('=========================\nIAC:', round(resulIac,2)) #Resultado
