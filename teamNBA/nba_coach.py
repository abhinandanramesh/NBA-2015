#!/usr/bin/env python
"""
nba_coach.py
:Author: Abhinandan Kelgere Ramesh
:Date: 11/11/2015
This module defines NBACoach class that aggregates 
the data from all the NBACoach collections and wraps it up in 
to a transactional format
"""

import csv

import sys
reload(sys)


class NBATransaction:
	"""
	This class consists of a transaction object corresponding to 
	the NBACoach data.This class object represents the data aggregated 
	over all the NBACoach collectionsand combined to a single class.
	Collection: 
	------------------------------------------------------------------------------
	coaches_career, coaches_season
	"""
	def __init__(self):
		self.Team = "None"
		self.Season = "None"
		self.coach_season_win_rate = "0"
		self.coach_career_win_rate = "0"
		
	def __str__(self):
		return "Team: %s , Season: %s , coach_season_win_rate: %s, coach_career_win_rate: %s" % (self.Team, self.Season, self.coach_season_win_rate, self.coach_career_win_rate)

	def __repr__(self):
		return "Team: %s , Season: %s , coach_season_win_rate: %s, coach_career_win_rate: %s" % (self.Team, self.Season, self.coach_season_win_rate, self.coach_career_win_rate)

	def convertNBAContent(self, team, season):
		"""
		Converts the data in NBA coach content into
		the transactional format and returns a NBA coach
		Content transaction object.
		"""

		self.Team = team
		self.Season = season

		coach_id = []
		
		f2 = open('coaches_season.txt')
		csv_f2 = csv.reader(f2)

		for row in csv_f2:
			if row[9] == team and row[1] == str(season):
				coach_id.append(row[0])

		f2.close()			

		coach_season_stat = []
		coach_career_stat = []
		temp_season = 0.0
		season = season - 1
		year = 2

		while (year > 0):
			for coach in coach_id:
				f2 = open('coaches_season.txt')
				csv_f2 = csv.reader(f2)
				for row in csv_f2:
					if row[0] == coach and row[1] == str(season):
						temp_season = 0.0
						temp_season = (float(row[5]) + float(row[7]))/(float(row[5]) + float(row[6]) + float(row[7]) + float(row[8]))
						coach_season_stat.append(temp_season)
						
				
				f2.close()	
			year = year - 1
			season = season - 1

		for coach in coach_id:
			f1 = open('coaches_career.txt')
			csv_f1 = csv.reader(f1)
			temp_season = 0.0
	
			for name in csv_f1:
				if coach == name[0]:
					temp_season = (float(name[3]) + float(name[5]))/(float(name[3]) + float(name[4]) + float(name[5]) + float(name[6]))
					if temp_season > 0: 
						coach_career_stat.append(temp_season)
					
					break
			f1.close()
							

		if len(coach_season_stat) > 0:
			self.coach_season_win_rate = str(sum(coach_season_stat)/len(coach_season_stat))		

		if len(coach_career_stat) > 0:
			self.coach_career_win_rate = str(sum(coach_career_stat)/len(coach_career_stat))

def createNBATransactions():
	"""
	Creates a list a NBACoach Content Transactions by 
	converting each document in the NBACoach
	collection and converting it to a transaction object.
	"""

	NBATransactions = []
	
	NBATeams = ['ATL','BOS','CHI', 'CHA','CLE','DAL','DEN','DET','GSW','HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NJN', 'NOH', 'NYK', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'SEA', 'TOR', 'UTA', 'WAS']

	NBASeasons = ['1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003']

	for team in NBATeams:
		for season in NBASeasons:
			NBADataTransaction = NBATransaction()
			NBADataTransaction.convertNBAContent(team, int(season))
			NBATransactions.append(NBADataTransaction)

	return NBATransactions


def convertToTransactions():
	"""
	Converts the NBACoach content into transactions and dumps into CSV
	in specified directory.
	"""
	Transactions = []
	Transactions.extend(createNBATransactions())

	with open('NBAcoachTransactions.csv','wb') as fp:
		writer = csv.writer(fp, delimiter=',')
		writer.writerow(["Team", "Season", "coach_season_win_rate", "coach_career_win_rate"])

		for transaction in Transactions:
			writer.writerow([transaction.Team, transaction.Season, transaction.coach_season_win_rate, transaction.coach_career_win_rate])

	return Transactions

convertToTransactions()
