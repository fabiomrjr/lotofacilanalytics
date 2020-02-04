import numpy as np
import matplotlib.pyplot as plt
import pandas

from Contest import Contest
from Game import Game

class GamesContestsCheck:

    def __init__(self, games, contests):
        self.games = games
        self.contests = contests
        self.compilado = np.zeros((len(games) * len(contests),4), dtype = object)

    def checkNumerosAcertados(self):
        i=0
        while i < (len(self.contests) * len(self.games)):
            for sorteio in self.contests:
                for jogo in self.games:
                    #dia, mess, ano = sorteio[1].split("/")
                    self.compilado[i,0] = str(sorteio.date.month) + ' - ' + str(sorteio.date.year);
                    self.compilado[i,1] = sorteio.id;
                    self.compilado[i,2] = jogo.id;

                    count = 0
                    for numeroSorteio in sorteio.numbers:
                        for numeroJogo in jogo.numbers:
                            if numeroJogo == numeroSorteio:
                                count = count + 1

                    # if int(sorteio.date.month) == self.mes:
                    #     for numeroSorteio in sorteio[2:17]:
                    #         for numeroJogo in jogo[1:16]:
                    #             if numeroJogo == numeroSorteio:
                    #                 count = count + 1
                    #     #self.compilado[i,2] = count
                    # elif self.mes == -1:
                    #     for numeroSorteio in sorteio[ 2:17 ]:
                    #         for numeroJogo in jogo[1:16]:
                    #             if numeroJogo == numeroSorteio:
                    #                 count = count + 1
                    self.compilado[i,3] = count
                    i = i + 1

        for comp in self.compilado:
            if comp[3] == 14 or comp[3] == 15 or comp[3] == 13:
                print(comp)