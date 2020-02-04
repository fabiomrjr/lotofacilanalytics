import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

class PlusOneMinusOnePeriod:

    def __init__(self, startContest, endContest, contests):
        self.startContest = int(startContest)
        self.endContest = int(endContest)
        self.contests = contests
        self.compilado = np.zeros((endContest - startContest,25))

    def process(self):
        count = 0;
        for contest in self.contests:
            if contest.id >= self.startContest and contest.id < self.endContest:
                if count != 0:
                    self.compilado[count, :] = self.compilado[count - 1, :]

                for number in range(1,26):
                    #for numberOnContest in contest.numbers:
                    if number in contest.numbers:
                        self.compilado[count, number - 1 ] = self.compilado[count, number - 1 ] + 1
                    else:
                        self.compilado[count, number - 1 ] = self.compilado[count, number - 1 ] - 1

                count = count + 1
        self.plotResults()

    def plotResults(self):
        fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))
        x = np.arange(self.startContest, self.endContest)

        axes[0,0].plot(x, self.compilado[:,0], label='Numero 1')
        axes[ 0, 0 ].plot(x, self.compilado[:,1], label='Numero 2')
        axes[ 0, 0 ].plot(x, self.compilado[:,2], label='Numero 3')
        axes[ 0, 0 ].plot(x, self.compilado[:,3], label='Numero 4')
        axes[ 0, 0 ].plot(x, self.compilado[:,4], label='Numero 5')
        axes[ 0, 0 ].grid()
        axes[ 0, 0 ].legend()

        axes[ 0, 1 ].plot(x, self.compilado[ :, 5 ], label='Numero 6')
        axes[ 0, 1 ].plot(x, self.compilado[ :, 6 ], label='Numero 7')
        axes[ 0, 1 ].plot(x, self.compilado[ :, 7 ], label='Numero 8')
        axes[ 0, 1 ].plot(x, self.compilado[ :, 8 ], label='Numero 9')
        axes[ 0, 1 ].plot(x, self.compilado[ :, 9 ], label='Numero 10')
        axes[ 0, 1 ].grid()
        axes[ 0, 1 ].legend()

        axes[ 1, 0 ].plot(x, self.compilado[ :, 10 ], label='Numero 11')
        axes[ 1, 0 ].plot(x, self.compilado[ :, 11 ], label='Numero 12')
        axes[ 1, 0 ].plot(x, self.compilado[ :, 12 ], label='Numero 13')
        axes[ 1, 0 ].plot(x, self.compilado[ :, 13 ], label='Numero 14')
        axes[ 1, 0 ].plot(x, self.compilado[ :, 14 ], label='Numero 15')
        axes[ 1, 0 ].grid()
        axes[ 1, 0 ].legend()

        axes[ 1, 1 ].plot(x, self.compilado[ :, 11 ], label='Numero 16')
        axes[ 1, 1 ].plot(x, self.compilado[ :, 12 ], label='Numero 17')
        axes[ 1, 1 ].plot(x, self.compilado[ :, 13 ], label='Numero 18')
        axes[ 1, 1 ].plot(x, self.compilado[ :, 14 ], label='Numero 19')
        axes[ 1, 1 ].plot(x, self.compilado[ :, 15 ], label='Numero 20')
        axes[ 1, 1 ].grid()
        axes[ 1, 1 ].legend()

        axes[ 2, 0 ].plot(x, self.compilado[ :, 16 ], label='Numero 21')
        axes[ 2, 0 ].plot(x, self.compilado[ :, 17 ], label='Numero 22')
        axes[ 2, 0 ].plot(x, self.compilado[ :, 18 ], label='Numero 23')
        axes[ 2, 0 ].plot(x, self.compilado[ :, 19 ], label='Numero 24')
        axes[ 2, 0 ].plot(x, self.compilado[ :, 20 ], label='Numero 25')
        axes[ 2, 0 ].grid()
        axes[ 2, 0 ].legend()

        plt.show()