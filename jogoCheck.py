import numpy as np

class JogoCheck:

    def __init__(self, jogos, resultados, mes):
        self.jogos = jogos
        self.resultados = resultados
        self.compilado = np.zeros((len(jogos) * len(resultados),4), dtype = object)
        self.mes = mes

    def checkNumerosAcertados(self):
        i=0
        while i < (len(self.resultados) * len(self.jogos)):
            for sorteio in self.resultados:

                for jogo in self.jogos:
                    dia, mess, ano = sorteio[1].split("/")
                    self.compilado[ i, 1 ] = str(mess) + ' - ' + str(ano);
                    self.compilado[i,2] = jogo[0];
                    self.compilado[i,0] = sorteio[0];


                    count = 0
                    if int(mess) == self.mes:
                        for numeroSorteio in sorteio[2:17]:
                            for numeroJogo in jogo[1:16]:
                                if numeroJogo == numeroSorteio:
                                    count = count + 1
                        #self.compilado[i,2] = count
                    elif self.mes == -1:
                        for numeroSorteio in sorteio[ 2:17 ]:
                            for numeroJogo in jogo[1:16]:
                                if numeroJogo == numeroSorteio:
                                    count = count + 1
                    self.compilado[i,3] = count
                    i = i + 1

        for comp in self.compilado:
            if comp[3] == 14 or comp[3] == 15 or comp[3] == 13:
                print(comp)