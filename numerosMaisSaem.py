import numpy as np
import matplotlib.pyplot as plt
import pandas


class NumerosMaisSaem:

    def __init__(self, mes, ano, resultados):
        self.mes = mes
        self.ano = ano
        self.resultados = resultados
        self.compilado = np.zeros((1,25))

    def process(self):

        for dataConcurso in self.resultados:
            dia, mes, ano = dataConcurso[1].split("/")

            resultadosSorteio = dataConcurso[3:18].astype(int)

            if self.mes == -1 and self.ano == -1:
                #for index in range(1, 26):
                for numero in resultadosSorteio:
                    self.compilado[0, numero - 1 ] = self.compilado[0, numero - 1 ] + 1
            elif self.mes != -1 and self.ano != -1:
                if int(mes) == self.mes and int(ano) == self.ano:
                    for numero in resultadosSorteio:
                        self.compilado[ 0, numero - 1 ] = self.compilado[ 0, numero - 1 ] + 1
            elif self.mes != -1:
                if int(mes) == self.mes:
                    for numero in resultadosSorteio:
                        self.compilado[ 0, numero - 1 ] = self.compilado[ 0, numero - 1 ] + 1
            elif self.ano != -1:
                if int(ano) == self.ano:
                    for numero in resultadosSorteio:
                        self.compilado[ 0, numero - 1 ] = self.compilado[ 0, numero - 1 ] + 1
        self.plotResults()

    def plotResults(self):
        fig, ax1 = plt.subplots()
        x = np.arange(1,26,1)
        line11 = ax1.plot(x, self.compilado[0,:], label='Vezes saiu')
        #line12 = ax1.plot(x, saiMenosUltimoMes[9,:], label='Ultimo Outubro Mais Saiu')
        ax1.grid()
        ax1.legend()
        plt.show()
