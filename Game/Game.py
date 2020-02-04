class Game:

    def __init__(self, id, numbers):
        self.id = id
        self.numbers = numbers #np.zeros((len(jogos) * len(resultados),4), dtype = object)

    def check(self, contest):
        for numeroSorteio in contest.numbers:
            for numeroJogo in self.numbers:
                if numeroJogo == numeroSorteio:
                    count = count + 1
        return count