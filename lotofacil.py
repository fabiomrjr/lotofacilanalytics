import numpy as np
import matplotlib.pyplot as plt
import pandas

from Contest import Contest
from Game import Game
from Analiser.NumbersMostDraft import NumbersMostDraft
from Analiser.NumberMostDraftByStepAndPeriod import NumberMostDraftByStepAndPeriod
from Analiser.PlusOneMinusOnePeriod import PlusOneMinusOnePeriod
from Analiser.PlusOneMinusOnPeriodAnalysis import PlusOneMinusOnePeriodAnalysis
from jogoCheck import JogoCheck
from numerosMaisSaem import NumerosMaisSaem
from dataLoader import DataLoader
from charBars import bar
from Analiser.GamesContestsCheck import GamesContestsCheck

contests = DataLoader("data/resultados.txt").loadData()
games = DataLoader("data/jogos.txt").loadTips()

#NumbersMostDraft(12, 2018, contests).process()
#NumberMostDraftByStepAndPeriod(5, 3, 1, contests).process()
#GamesContestsCheck(games, contests).checkNumerosAcertados()
plusOneMinusOnePeriodAnalysisItem = PlusOneMinusOnePeriodAnalysis()
plusOneMinusOnePeriodAnalysisItem.defineVariables(1683, 1803, 12, contests)
plusOneMinusOnePeriodAnalysisItem.process()

plusOneMinusOnePeriodAnalysisItem2 = PlusOneMinusOnePeriodAnalysis()
plusOneMinusOnePeriodAnalysisItem2.defineVariablesPeriods(1803, 1815, 1780, 1792, 12, contests)
plusOneMinusOnePeriodAnalysisItem2.processPeriods()


