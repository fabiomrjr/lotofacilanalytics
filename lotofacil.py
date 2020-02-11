from Analiser.GamesContestsCheck import GamesContestsCheck
from Analiser.MostWinningGames import MostWinningGames
from dataLoader import DataLoader

contests = DataLoader("data/resultados1.txt").loadData()
games = DataLoader("data/jogos.txt").loadTips()

#NumbersMostDraft(12, 2018, contests).process()
#NumberMostDraftByStepAndPeriod(5, 3, 1, contests).process()
GamesContestsCheck(games, contests).checkNumerosAcertados()
#MostWinningGames(contests).process()
#plusOneMinusOnePeriodAnalysisItem = PlusOneMinusOnePeriodAnalysis()
#plusOneMinusOnePeriodAnalysisItem.defineVariables(1683, 1803, 12, contests)
#plusOneMinusOnePeriodAnalysisItem.process()

#plusOneMinusOnePeriodAnalysisItem2 = PlusOneMinusOnePeriodAnalysis()
#plusOneMinusOnePeriodAnalysisItem2.defineVariablesPeriods(1803, 1815, 1780, 1792, 12, contests)
#plusOneMinusOnePeriodAnalysisItem2.processPeriods()


