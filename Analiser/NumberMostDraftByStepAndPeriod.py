import numpy as np
import matplotlib.pyplot as plt
import pandas

from Contest import Contest
from Game import Game

class NumberMostDraftByStepAndPeriod:

    def __init__(self, period, step, delay, contests):
        self.period = period
        self.step = step
        self.contests = contests
        self.delay = delay
        self.compilado = np.zeros((step,25))

    def process(self):
        for aux in range(self.delay, (self.period * self.step) + self.delay):
            for step in range(0, self.step):
                if aux < (((step + 1) * self.period) + self.delay):
                    for number in self.contests[aux].numbers:
                        self.compilado[step, number - 1 ] = self.compilado[step, number - 1 ] + 1

        for step in range(1, self.step + 1):
            self.compilado[step - 1, :] = self.compilado[step - 1, :] * 100 / (step * self.period)

        self.plotResults()

    def plotResults(self):
        fig, ax1 = plt.subplots()
        x = np.arange(1,26,1)
        for aux in range(0,self.step):
            leng = (aux + 1) * self.period
            ax1.plot(x, self.compilado[aux,:], label='{} ultimos concursos'.format(leng))
        ax1.grid()
        ax1.legend()
        #line12 = ax1.plot(x, saiMenosUltimoMes[9,:], label='Ultimo Outubro Mais Saiu')
        #ax1.grid()
        #ax1.legend()
        plt.show()