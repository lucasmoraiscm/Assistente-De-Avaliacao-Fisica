from tkinter import *
from controller import *


#Inicializar IMC
def btn_clickImc():
    janelaHome.destroy()

    #Cálculo IMC
    def btn_clickCalcImc():
        massaImc = float(ed_massaImc.get())
        alturaImc = float(ed_alturaImc.get())
        respViewImc = ImcController.calcularImcController(massaImc, alturaImc)
        lb_respImc['text'] = respViewImc

    #janela IMC
    janelaImc = Tk()
    janelaImc.geometry('500x500+300+300')
    janelaImc.title('IMC')

    lb_Imc1 = Label(janelaImc, text = 'Massa(Kg):')
    lb_Imc1.place(x = 10,y = 20)
    ed_massaImc = Entry(janelaImc, bg = 'white')
    ed_massaImc.place(x = 100,y = 20)

    lb_Imc2 = Label(janelaImc, text = 'Altura(m):')
    lb_Imc2.place(x = 10, y = 50)
    ed_alturaImc = Entry(janelaImc, bg = 'white')
    ed_alturaImc.place(x = 100, y = 50)

    lb_respImc = Label(janelaImc, bg = 'white', width = 10, text = '')
    lb_respImc.place(x = 100, y = 80)

    btn_Imc = Button(janelaImc, text = 'Calcular', width = 10, command = btn_clickCalcImc)
    btn_Imc.place(x = 85, y = 120)
 
    janelaImc.mainloop()


#Inicializar RCQ
def btn_clickRcq():
    janelaHome.destroy()

    #Cálculo RCQ
    def btn_clickCalcRcq():
        cinturaRcq = float(ed_cinturaRcq.get())
        quadrilRcq = float(ed_quadrilRcq.get())
        respViewRcq = RcqController.calcularRcqController(cinturaRcq, quadrilRcq)
        lb_respRcq['text'] = respViewRcq

    #Janela RCQ
    janelaRcq = Tk()
    janelaRcq.geometry('500x500+300+300')
    janelaRcq.title('RCQ')

    lb_Rcq1 = Label(janelaRcq, text = 'Cintura(cm):')
    lb_Rcq1.place(x = 10,y = 20)
    ed_cinturaRcq = Entry(janelaRcq, bg = 'white')
    ed_cinturaRcq.place(x = 100,y = 20)

    lb_Rcq2 = Label(janelaRcq, text = 'Quadril(cm):')
    lb_Rcq2.place(x = 10, y = 50)
    ed_quadrilRcq = Entry(janelaRcq, bg = 'white')
    ed_quadrilRcq.place(x = 100, y = 50)

    lb_respRcq = Label(janelaRcq, bg = 'white', width = 10, text = '')
    lb_respRcq.place(x = 100, y = 80)

    btn_Rcq = Button(janelaRcq, text = 'Calcular', width = 10, command = btn_clickCalcRcq)
    btn_Rcq.place(x = 85, y = 120)

    janelaRcq.mainloop()


#Inicializar IAC
def btn_clickIac():
    janelaHome.destroy()

    #Cálculo IAC
    def btn_clickCalcIac():
        quadrilIac = float(ed_quadrilIac.get())
        alturaIac = float(ed_alturaIac.get())
        respViewIac = IacController.calcularIacController(quadrilIac, alturaIac)
        lb_respIac['text'] = respViewIac

    #Janela IAC
    janelaIac = Tk()
    janelaIac.geometry('500x500+300+300')
    janelaIac.title('IAC')

    lb_Iac1 = Label(janelaIac, text = 'Quadril(cm):')
    lb_Iac1.place(x = 10,y = 20)
    ed_quadrilIac = Entry(janelaIac, bg = 'white')
    ed_quadrilIac.place(x = 100,y = 20)

    lb_Iac2 = Label(janelaIac, text = 'Altura(m):')
    lb_Iac2.place(x = 10, y = 50)
    ed_alturaIac = Entry(janelaIac, bg = 'white')
    ed_alturaIac.place(x = 100, y = 50)

    lb_respIac = Label(janelaIac, bg = 'white', width = 10, text = '')
    lb_respIac.place(x = 100, y = 80)

    btn_Iac = Button(janelaIac, text = 'Calcular', width = 10, command = btn_clickCalcIac)
    btn_Iac.place(x = 85, y = 120)

    janelaIac.mainloop()


#Home
janelaHome = Tk()
janelaHome.geometry('500x500+300+300')
janelaHome.title('Assistente de Avaliação Física')

lb_Home = Label(janelaHome, text = 'Escolha a opção desejada:')
lb_Home.place(x = 10,y = 10)

btn_HomeImc = Button(janelaHome, text = 'IMC', width = 10, command = btn_clickImc)
btn_HomeImc.place(x = 40, y = 40)

btn_HomeRcq = Button(janelaHome, text = 'RCQ', width = 10, command = btn_clickRcq)
btn_HomeRcq.place(x = 40, y = 70)

btn_HomeIac = Button(janelaHome, text = 'IAC', width = 10, command = btn_clickIac)
btn_HomeIac.place(x = 40, y = 100)

janelaHome.mainloop()
