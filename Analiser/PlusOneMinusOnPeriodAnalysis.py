import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

class PlusOneMinusOnePeriodAnalysis:

    def __init__(self):
        startContestMain = 0
        endContestMain = 0
        startContest = 0
        endContest = 0
        contests = None
        step = 0
        coeficient = 0

    def defineVariables(self, startContest, endContest, step, contests):
        self.startContest = int(startContest)
        self.endContest = int(endContest)
        self.contests = contests
        self.step = int(step)
        self.coeficient = (endContest - startContest) / step

        if float(self.coeficient).is_integer():
            self.coeficient = int(self.coeficient)
            self.compilado = np.zeros((self.coeficient, 28))
        else:
            print("Coeficient is not a integer.")

    def defineVariablesPeriods(self, startContestMain, endContestMain, startContest, endContest, step, contests):
        self.startContestMain = int(startContestMain)
        self.endContestMain = int(endContestMain)
        self.startContest = int(startContest)
        self.endContest = int(endContest)
        self.contests = contests
        self.step = int(step)
        self.coeficient = ((endContestMain - startContestMain) + (endContest - startContest)) / step

        if float(self.coeficient).is_integer():
            self.coeficient = int(self.coeficient)
            self.compilado = np.zeros((self.coeficient, 28))
        else:
            print("Coeficient is not a integer.")

    def process(self):
        count = 0;
        countContest = 0;

        if float(self.coeficient).is_integer():
            for contest in self.contests:
                start = (self.endContest - self.step * countContest)
                end = (self.endContest - self.step * (countContest + 1))


                if contest.id > (self.startContest) and contest.id <= (self.endContest) and contest.id <= start and contest.id > end:
                    for number in range(1,26):
                        #for numberOnContest in contest.numbers:
                        if number in contest.numbers:
                            self.compilado[countContest, number + 2 ] = self.compilado[countContest, number + 2 ] + 1
                        else:
                            self.compilado[countContest, number + 2 ] = self.compilado[countContest, number + 2 ] - 1

                    if count == 0:
                        self.compilado[countContest, 0] = contest.id
                    if count == 11:
                        self.compilado[countContest, 1] = contest.id
                        count = -1
                        countContest = countContest + 1
                    count = count + 1

            for number in range(0, self.coeficient):
                self.compilado[number, 2] = mean_squared_error(self.compilado[0, 3:27], self.compilado[number, 3:27])

            for item in self.compilado:
                if item[2] <= 15:
                    print(item[0:3])

    def processPeriods(self):
        #Desenvolver
        count = 0;
        countContest = 0;

        if float(self.coeficient).is_integer():
            for contest in self.contests:
                if self.endContest > self.endContestMain:
                    start = (self.endContest - self.step * countContest)
                else:
                    start = (self.endContestMain - self.step * countContest)

                if self.endContest > self.endContestMain:
                    start = (self.endContestMain - self.step * (countContest + 1))
                else:
                    end = (self.endContest - self.step * (countContest + 1))

                isInsidePeriods = ((contest.id > self.startContest and contest.id <= self.endContest) or (contest.id > self.startContestMain and contest.id <= self.endContestMain))

                if isInsidePeriods and contest.id <= start and contest.id > end:
                    for number in range(1, 26):
                        # for numberOnContest in contest.numbers:
                        if number in contest.numbers:
                            self.compilado[ countContest, number + 2 ] = self.compilado[ countContest, number + 2 ] + 1
                        else:
                            self.compilado[ countContest, number + 2 ] = self.compilado[ countContest, number + 2 ] - 1

                    if count == 0:
                        self.compilado[ countContest, 0 ] = contest.id
                    if count == 11:
                        self.compilado[ countContest, 1 ] = contest.id
                        count = -1
                        countContest = countContest + 1
                    count = count + 1

            for number in range(0, self.coeficient):
                self.compilado[ number, 2 ] = mean_squared_error(self.compilado[ 0, 3:27 ], self.compilado[ number, 3:27 ])
            print(self.compilado)