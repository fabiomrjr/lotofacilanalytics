import numpy as np

class Contest:

    def __init__(self, id, date, location, numbers):
        self.id = int(id)
        self.date = date
        self.location = location
        self.numbers = numbers #np.zeros((len(jogos) * len(resultados),4), dtype = object)

    def getNumbersDraftArray(self):
        compilado = np.zeros((1,25))

        for number in self.numbers:
            self.compilado[ 0, number - 1 ] = self.compilado[ 0, number - 1 ] + 1
        return compilado