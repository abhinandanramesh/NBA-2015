#!/usr/bin/env python
"""
nba_coach.py
:Author: Abhinandan Kelgere Ramesh
:Date: 11/11/2015
This module defines NBAPlayers class that aggregates 
the data from all the NBAPlayers collections and wraps it up in 
to a transactional format.
"""

import csv

import sys
reload(sys)


class NBATransaction:
	"""
	This class consists of a transaction object corresponding to 
	the NBAPlayers data.This class object represents the data aggregated 
	over all the NBAPlayers collectionsand combined to a single class.
	Collection: 
	------------------------------------------------------------------------------
	coaches_career, coaches_season
	"""
	def __init__(self):
		self.Team = "None"
		self.Season = "None"
		self.season_gp = "0"
		self.season_minutes = "0"
		self.season_pts = "0"
		self.season_dreb = "0"
		self.season_oreb = "0"
		self.season_reb = "0"
		self.season_asts = "0"
		self.season_stl = "0"
		self.season_blk = "0"
		self.season_turnover = "0"
		self.season_pf = "0"
		self.season_fga = "0"
		self.season_fgm = "0"
		self.season_fta = "0"
		self.season_ftm = "0"
		self.season_tpa = "0"
		self.season_tpm = "0"
		self.career_gp = "0"
		self.career_minutes = "0"
		self.career_pts = "0"
		self.career_dreb = "0"
		self.career_oreb = "0"
		self.career_reb = "0"
		self.career_asts = "0"
		self.career_stl = "0"
		self.career_blk = "0"
		self.career_turnover = "0"
		self.career_pf = "0"
		self.career_fga = "0"
		self.career_fgm = "0"
		self.career_fta = "0"
		self.career_ftm = "0"
		self.career_tpa = "0"
		self.career_tpm = "0"
		
	def __str__(self):
		return "Team: %s , Season: %s , season_gp: %s, season_minutes: %s, season_pts: %s, season_dreb: %s, season_oreb: %s, season_reb: %s, season_asts: %s, season_stl: %s, season_blk: %s, season_turnover: %s, season_pf: %s, season_fga: %s, season_fgm: %s, season_fta: %s, season_ftm: %s, season_tpa: %s, season_tpm: %s, career_gp: %s, career_minutes: %s, career_pts: %s, career_dreb: %s, career_oreb: %s, career_reb: %s, career_asts: %s, career_stl: %s, career_blk: %s, career_turnover: %s, career_pf: %s, career_fga: %s, career_fgm: %s, career_fta: %s, career_ftm: %s, career_tpa: %s, career_tpm: %s" % (self.Team, self.Season, self.season_gp, self.season_minutes, self.season_pts, self.season_dreb, self.season_oreb, self.season_reb, self.season_asts, self.season_stl, self.season_blk, self.season_turnover, self.season_pf, self.season_fga, self.season_fgm, self.season_fta, self.season_ftm, self.season_tpa, self.season_tpm, self.career_gp, self.career_minutes, self.career_pts, self.career_dreb, self.career_oreb, self.career_reb, self.career_asts, self.career_stl, self.career_blk, self.career_turnover, self.career_pf, self.career_fga, self.career_fgm, self.career_fta, self.career_ftm, self.career_tpa, self.career_tpm)

	def __repr__(self):
		return "Team: %s , Season: %s , season_gp: %s, season_minutes: %s, season_pts: %s, season_dreb: %s, season_oreb: %s, season_reb: %s, season_asts: %s, season_stl: %s, season_blk: %s, season_turnover: %s, season_pf: %s, season_fga: %s, season_fgm: %s, season_fta: %s, season_ftm: %s, season_tpa: %s, season_tpm: %s, career_gp: %s, career_minutes: %s, career_pts: %s, career_dreb: %s, career_oreb: %s, career_reb: %s, career_asts: %s, career_stl: %s, career_blk: %s, career_turnover: %s, career_pf: %s, career_fga: %s, career_fgm: %s, career_fta: %s, career_ftm: %s, career_tpa: %s, career_tpm: %s" % (self.Team, self.Season, self.season_gp, self.season_minutes, self.season_pts, self.season_dreb, self.season_oreb, self.season_reb, self.season_asts, self.season_stl, self.season_blk, self.season_turnover, self.season_pf, self.season_fga, self.season_fgm, self.season_fta, self.season_ftm, self.season_tpa, self.season_tpm, self.career_gp, self.career_minutes, self.career_pts, self.career_dreb, self.career_oreb, self.career_reb, self.career_asts, self.career_stl, self.career_blk, self.career_turnover, self.career_pf, self.career_fga, self.career_fgm, self.career_fta, self.career_ftm, self.career_tpa, self.career_tpm)

	def convertNBAContent(self, team, season):
		"""
		Converts the data in NBAPlayers content into
		the transactional format and returns a NBA coach
		Content transaction object.
		"""

		self.Team = team
		self.Season = season

		player_id = []
		
		f2 = open('player_playoffs.txt')
		csv_f2 = csv.reader(f2)

		for row in csv_f2:
			if row[4] == team and row[1] == str(season):
				if row[0] not in player_id:
					player_id.append(row[0])

		f2.close()			

		f1 = open('player_regular_season.txt')
		csv_f1 = csv.reader(f1)

		for row in csv_f1:
			if row[4] == team and row[1] == str(season):
				if row[0] not in player_id:
					player_id.append(row[0])

		f1.close()			

		player_season_stat = [0] * 17
		player_career_stat = [0] * 17
		season = season - 1
		numberSeason = 0
		numberCareer = 0
		year = 2

		while (year > 0):
			for player in player_id:
				f2 = open('player_playoffs.txt')
				csv_f2 = csv.reader(f2)
				for row in csv_f2:
					if row[0] == player and row[1] == str(season):
						numberSeason += 1
						player_season_stat[0] += int(row[6])
						player_season_stat[1] += int(row[7])
						player_season_stat[2] += int(row[8])
						player_season_stat[3] += int(row[9])
						player_season_stat[4] += int(row[10])
						player_season_stat[5] += int(row[11])
						player_season_stat[6] += int(row[12])
						player_season_stat[7] += int(row[13])
						player_season_stat[8] += int(row[14])
						player_season_stat[9] += int(row[15])
						player_season_stat[10] += int(row[16])
						player_season_stat[11] += int(row[17])
						player_season_stat[12] += int(row[18])
						player_season_stat[13] += int(row[19])
						player_season_stat[14] += int(row[20])
						player_season_stat[15] += int(row[21])
						player_season_stat[16] += int(row[22])	
						break					
				
				f2.close()

				f2 = open('player_regular_season.txt')
				csv_f2 = csv.reader(f2)
				for row in csv_f2:
					if row[0] == player and row[1] == str(season):
						numberSeason += 1
						player_season_stat[0] += int(row[6])
						player_season_stat[1] += int(row[7])
						player_season_stat[2] += int(row[8])
						player_season_stat[3] += int(row[9])
						player_season_stat[4] += int(row[10])
						player_season_stat[5] += int(row[11])
						player_season_stat[6] += int(row[12])
						player_season_stat[7] += int(row[13])
						player_season_stat[8] += int(row[14])
						player_season_stat[9] += int(row[15])
						player_season_stat[10] += int(row[16])
						player_season_stat[11] += int(row[17])
						player_season_stat[12] += int(row[18])
						player_season_stat[13] += int(row[19])
						player_season_stat[14] += int(row[20])
						player_season_stat[15] += int(row[21])
						player_season_stat[16] += int(row[22])	
						break					
				
				f2.close()
	

			year = year - 1
			season = season - 1

		for player in player_id:
			f3 = open('player_playoffs_career.txt')
			csv_f3 = csv.reader(f3)
			for row in csv_f3:
				if row[0] == player:
					numberCareer += 1
					player_career_stat[0] += int(row[4])
					player_career_stat[1] += int(row[5])
					player_career_stat[2] += int(row[6])
					player_career_stat[3] += int(row[7])
					player_career_stat[4] += int(row[8])
					player_career_stat[5] += int(row[9])
					player_career_stat[6] += int(row[10])
					player_career_stat[7] += int(row[11])
					player_career_stat[8] += int(row[12])
					player_career_stat[9] += int(row[13])
					player_career_stat[10] += int(row[14])
					player_career_stat[11] += int(row[15])
					player_career_stat[12] += int(row[16])
					player_career_stat[13] += int(row[17])
					player_career_stat[14] += int(row[18])
					player_career_stat[15] += int(row[19])
					player_career_stat[16] += int(row[10])
					break						
				
			f3.close()	

			f3 = open('player_regular_season_career.txt')
			csv_f3 = csv.reader(f3)
			for row in csv_f3:
				if row[0] == player:
					numberCareer += 1
					player_career_stat[0] += int(row[4])
					player_career_stat[1] += int(row[5])
					player_career_stat[2] += int(row[6])
					player_career_stat[3] += int(row[7])
					player_career_stat[4] += int(row[8])
					player_career_stat[5] += int(row[9])
					player_career_stat[6] += int(row[10])
					player_career_stat[7] += int(row[11])
					player_career_stat[8] += int(row[12])
					player_career_stat[9] += int(row[13])
					player_career_stat[10] += int(row[14])
					player_career_stat[11] += int(row[15])
					player_career_stat[12] += int(row[16])
					player_career_stat[13] += int(row[17])
					player_career_stat[14] += int(row[18])
					player_career_stat[15] += int(row[19])
					player_career_stat[16] += int(row[20])
					break						
				
			f3.close()	
							

		if numberSeason > 0:
			self.season_gp = str(player_season_stat[0]/numberSeason)
			self.season_minutes = str(player_season_stat[1]/numberSeason)
			self.season_pts = str(player_season_stat[2]/numberSeason)
			self.season_dreb = str(player_season_stat[3]/numberSeason)
			self.season_oreb = str(player_season_stat[4]/numberSeason)
			self.season_reb = str(player_season_stat[5]/numberSeason)
			self.season_asts = str(player_season_stat[6]/numberSeason)
			self.season_stl = str(player_season_stat[7]/numberSeason)
			self.season_blk = str(player_season_stat[8]/numberSeason)
			self.season_turnover = str(player_season_stat[9]/numberSeason)
			self.season_pf = str(player_season_stat[10]/numberSeason)
			self.season_fga = str(player_season_stat[11]/numberSeason)
			self.season_fgm = str(player_season_stat[12]/numberSeason)
			self.season_fta = str(player_season_stat[13]/numberSeason)
			self.season_ftm = str(player_season_stat[14]/numberSeason)
			self.season_tpa = str(player_season_stat[15]/numberSeason)
			self.season_tpm = str(player_season_stat[16]/numberSeason)
		

		if numberCareer > 0:
			self.career_gp = str(player_career_stat[0]/numberCareer)
			self.career_minutes = str(player_career_stat[1]/numberCareer)
			self.career_pts = str(player_career_stat[2]/numberCareer)
			self.career_dreb = str(player_career_stat[3]/numberCareer)
			self.career_oreb = str(player_career_stat[4]/numberCareer)
			self.career_reb = str(player_career_stat[5]/numberCareer)
			self.career_asts = str(player_career_stat[6]/numberCareer)
			self.career_stl = str(player_career_stat[7]/numberCareer)
			self.career_blk = str(player_career_stat[8]/numberCareer)
			self.career_turnover = str(player_career_stat[9]/numberCareer)
			self.career_pf = str(player_career_stat[10]/numberCareer)
			self.career_fga = str(player_career_stat[11]/numberCareer)
			self.career_fgm = str(player_career_stat[12]/numberCareer)
			self.career_fta = str(player_career_stat[13]/numberCareer)
			self.career_ftm = str(player_career_stat[14]/numberCareer)
			self.career_tpa = str(player_career_stat[15]/numberCareer)
			self.career_tpm = str(player_career_stat[16]/numberCareer)
			

def createNBATransactions():
	"""
	Creates a list a NBAPlayers Content Transactions by 
	converting each document in the NBAPlayers
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
	Converts the NBAPlayers content into transactions and dumps into CSV
	in specified directory.
	"""
	Transactions = []
	Transactions.extend(createNBATransactions())

	with open('NBAPlayerTransactions.csv','wb') as fp:
		writer = csv.writer(fp, delimiter=',')
		writer.writerow(["Team", "Season", "player_season_gp", "player_season_minutes", "player_season_pts", "player_season_dreb", "player_season_oreb", "player_season_reb", "player_season_asts", "player_season_stl", "player_season_blk", "player_season_turnover", "player_season_pf", "player_season_fga", "player_season_fgm", "player_season_fta", "player_season_ftm", "player_season_tpa", "player_season_tpm", "player_career_gp", "player_career_minutes", "player_career_pts", "player_career_dreb", "player_career_oreb", "player_career_reb", "player_career_asts", "player_career_stl", "player_career_blk", "player_career_turnover", "player_career_pf", "player_career_fga", "player_career_fgm", "player_career_fta", "player_career_ftm", "player_career_tpa", "player_career_tpm"])

		for transaction in Transactions:
			writer.writerow([transaction.Team, transaction.Season, transaction.season_gp, transaction.season_minutes, transaction.season_pts, transaction.season_dreb, transaction.season_oreb, transaction.season_reb, transaction.season_asts, transaction.season_stl, transaction.season_blk, transaction.season_turnover, transaction.season_pf, transaction.season_fga, transaction.season_fgm, transaction.season_fta, transaction.season_ftm, transaction.season_tpa, transaction.season_tpm, transaction.career_gp, transaction.career_minutes, transaction.career_pts, transaction.career_dreb, transaction.career_oreb, transaction.career_reb, transaction.career_asts, transaction.career_stl, transaction.career_blk, transaction.career_turnover, transaction.career_pf, transaction.career_fga, transaction.career_fgm, transaction.career_fta, transaction.career_ftm, transaction.career_tpa, transaction.career_tpm])

	return Transactions

convertToTransactions()
