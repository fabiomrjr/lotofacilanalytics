import numpy as np
from datetime import datetime
from Contest.Contest import Contest
from Game.Game import Game

class DataLoader:

    def __init__(self, filelocation):
        self.filelocation = filelocation

    def loadData(self):
        arquivo = np.loadtxt(self.filelocation, dtype='str', delimiter='\t', skiprows=1)
        #resultados = arquivo[ :, 3:18 ]
        #dados = np.column_stack((arquivo[ :, 0:2 ], resultados))
        lista = []

        for concurso in arquivo:
            dateContest = datetime.strptime(concurso[1], '%d/%m/%Y')
            contestaux = Contest(concurso[0], dateContest, concurso[2], concurso[3:18].astype(int))
            lista.append(contestaux)

        return lista

    def loadTips(self):
        jogos = np.loadtxt(self.filelocation, dtype='str', delimiter='\t',skiprows=1)
        lista = list()

        for jogo in jogos:
            game = Game(jogo[0], jogo[1:16].astype(int))
            lista.append(game)

        return lista