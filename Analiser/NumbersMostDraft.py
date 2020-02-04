import numpy as np
import matplotlib.pyplot as plt
import pandas

from Contest import Contest
from Game import Game

class NumbersMostDraft:

    def __init__(self, mes, ano, contests):
        self.mes = mes
        self.ano = ano
        self.contests = contests
        self.compilado = np.zeros((1,25))

    def process(self):
        for contest in self.contests:
            #resultadosSorteio = dataConcurso[3:18].astype(int)

            if self.mes == -1 and self.ano == -1:
                for number in contest.numbers:
                    self.compilado[0, number - 1 ] = self.compilado[0, number - 1 ] + 1
            elif self.mes != -1 and self.ano != -1:
                if int(contest.date.month) == self.mes and int(contest.date.year) == self.ano:
                    for number in contest.numbers:
                        self.compilado[ 0, number - 1 ] = self.compilado[ 0, number - 1 ] + 1
            elif self.mes != -1:
                if int(contest.date.month) == self.mes:
                    for number in contest.numbers:
                        self.compilado[ 0, number - 1 ] = self.compilado[ 0, number - 1 ] + 1
            elif self.ano != -1:
                if int(contest.date.year) == self.ano:
                    for number in contest.numbers:
                        self.compilado[ 0, number - 1 ] = self.compilado[ 0, number - 1 ] + 1
        self.plotResults()

    def plotResults(self):
        fig, ax1 = plt.subplots()
        x = np.arange(1,26,1)
        line11 = ax1.plot(x, self.compilado[0,:], label='Vezes saiu')
        #line12 = ax1.plot(x, saiMenosUltimoMes[9,:], label='Ultimo Outubro Mais Saiu')
        ax1.grid()
        ax1.legend()
        plt.show()