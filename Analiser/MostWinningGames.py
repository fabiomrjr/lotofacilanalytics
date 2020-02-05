import numpy as np
import matplotlib.pyplot as plt
import pandas

from Contest import Contest
from Game import Game

class MostWinningGames:

    def __init__(self, contests):
        self.contests = contests
        dataTypes = np.dtype([ ('name', 'S20'), ('age', 'i4') ])
        #a = np.array([ ('abc', 21, 50), ('xyz', 18, 75) ], dtype=dataTypes)
        self.compilado = np.empty([len(contests), 2], dtype = object)#dtype=dataTypes)
        self.compilado.fill("")
        #self.compilado = np.zeros([ len(contests), 2 ])

    def process(self):
        for contest in self.contests:
            contestNumbersString = "";

            for number in contest.numbers:
                contestNumbersString = contestNumbersString + str(number) + "-";

            isToCreate = True;

            for compiladoAux in range(len(self.compilado)):
                if self.compilado[compiladoAux, 0] == contestNumbersString:
                    self.compilado[ compiladoAux, 1] = self.compilado[compiladoAux, 1] + 1;
                    isToCreate = False;

                if isToCreate == True and self.compilado[compiladoAux, 0] == "":
                    self.compilado[compiladoAux, 0] = contestNumbersString;
                    self.compilado[ compiladoAux, 1] = 1;
                    break;

        self.plotResults()

    def plotResults(self):

        for dado in self.compilado:
            if dado[1] > 1:
                print(self.compilado)
        #fig, ax1 = plt.subplots()
        #x = np.arange(1,26,1)
        #line11 = ax1.plot(x, self.compilado[0,:], label='Vezes saiu')
        ##line12 = ax1.plot(x, saiMenosUltimoMes[9,:], label='Ultimo Outubro Mais Saiu')
        #ax1.grid()
        #ax1.legend()
        #plt.show()