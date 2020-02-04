import numpy as np
import matplotlib.pyplot as plt


class bar:

    def __init__(self):
        men_means, men_std = (20, 35, 30, 35, 27, 20, 21, 24, 20, 21, 24, 20, 35, 30, 35, 27, 20, 21, 24, 20, 21, 24, 24, 20, 24), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        women_means, women_std = (25, 32, 34, 20, 25, 20, 21, 24, 20, 21, 24, 20, 35, 30, 35, 27, 20, 21, 24, 20, 21, 24, 20, 21, 24), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        w, ws = (25, 32, 34, 20, 25, 20, 21, 24, 20, 21, 24, 20, 35, 30, 35, 27, 20, 21, 24, 20, 21, 24, 20, 21, 24), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        ind = np.arange(1,len(men_means)+1,1)  # the x locations for the groups
        width = 0.2  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind - 0.2, men_means, width, yerr=men_std, color='SkyBlue', label='Men')
        rects2 = ax.bar(ind, women_means, width, yerr=women_std, color='IndianRed', label='Women')
        rects3 = ax.bar(ind + 0.2, w, width, yerr=ws, color='Green', label='W')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(ind)
        #ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
        ax.legend()
        plt.show()