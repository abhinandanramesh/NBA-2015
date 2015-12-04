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
		self.Season = "None"
		self.Player = "None"
		self.player_pts = "0"
		self.player_reb = "0"
		self.player_asts = "0"
		self.player_stl = "0"
		self.player_blk = "0"
		self.player_turnover = "0"
		self.player_pf = "0"
		self.player_fg = "0"
		self.player_ft = "0"
		self.player_tp = "0"
		self.player_fgp = "0"
		self.player_ftp = "0"
		self.player_tpp = "0"		
		
	def __str__(self):
		return "Season: %s , Player: %s , player_pts: %s, player_reb: %s, player_asts: %s, player_stl: %s, player_blk: %s, player_turnover: %s, player_pf: %s, player_fg: %s, player_ft: %s, player_tp: %s, player_fgp: %s, player_ftp: %s, player_tpp: %s" % (self.Season, self.Player, self.player_pts, self.player_reb, self.player_asts, self.player_stl, self.player_blk, self.player_turnover, self.player_pf, self.player_fg, self.player_ft, self.player_tp, self.player_fgp, self.player_ftp, self.player_tpp)

	def __repr__(self):
		return "Season: %s , Player: %s , player_pts: %s, player_reb: %s, player_asts: %s, player_stl: %s, player_blk: %s, player_turnover: %s, player_pf: %s, player_fg: %s, player_ft: %s, player_tp: %s, player_fgp: %s, player_ftp: %s, player_tpp: %s" % (self.Season, self.Player, self.player_pts, self.player_reb, self.player_asts, self.player_stl, self.player_blk, self.player_turnover, self.player_pf, self.player_fg, self.player_ft, self.player_tp, self.player_fgp, self.player_ftp, self.player_tpp)

	def convertNBAContent(self, season, player):
		"""
		Converts the data in NBAPlayers content into
		the transactional format and returns a NBA coach
		Content transaction object.
		""" 
		self.Season = season
		self.Player = player
		
		player_season_stat = [0] * 10
		player_career_stat = [0] * 10

		f2 = open('player_regular_season.txt')
		csv_f2 = csv.reader(f2)
		fgp = 0.0
		ftp = 0.0
		tpp = 0.0
	
		for row in csv_f2:
			if row[0] == player and row[1] == season:
				#print player
				player_season_stat[0] += int(row[8])
				player_season_stat[1] += int(row[11])
				player_season_stat[2] += int(row[12])
				player_season_stat[3] += int(row[13])
				player_season_stat[4] += int(row[14])
				player_season_stat[5] += int(row[15])
				player_season_stat[6] += int(row[16])
				player_season_stat[7] += int(row[18])
				if int(row[17]) is not 0:
					fgp += float(row[18])/float(row[17])
				player_season_stat[8] += int(row[20])
				if int(row[19]) is not 0:
					ftp += float(row[20])/float(row[19])
				player_season_stat[9] += int(row[22])
				if int(row[21]) is not 0:
					tpp += float(row[22])/float(row[21])
				
		f2.close()

		f2 = open('player_playoffs.txt')
		csv_f2 = csv.reader(f2)

		for row in csv_f2:
			if row[0] == player and row[1] == season:
				#print player
				player_career_stat[0] += int(row[8])
				player_career_stat[1] += int(row[11])
				player_career_stat[2] += int(row[12])
				player_career_stat[3] += int(row[13])
				player_career_stat[4] += int(row[14])
				player_career_stat[5] += int(row[15])
				player_career_stat[6] += int(row[16])
				player_career_stat[7] += int(row[18])
				player_career_stat[8] += int(row[20])
				player_career_stat[9] += int(row[22])
				if int(row[17]) is not 0:
					fgp += float(row[18])/float(row[17])
				if int(row[19]) is not 0:
					ftp += float(row[20])/float(row[19])
				if int(row[21]) is not 0:
					tpp += float(row[22])/float(row[21])
				
		f2.close()

		self.player_pts = str(player_season_stat[0] + player_career_stat[0])
		self.player_reb = str(player_season_stat[1] + player_career_stat[1])
		self.player_asts = str(player_season_stat[2] + player_career_stat[2])
		self.player_stl = str(player_season_stat[3] + player_career_stat[3])
		self.player_blk = str(player_season_stat[4] + player_career_stat[4])
		self.player_turnover = str(player_season_stat[5] + player_career_stat[5])
		self.player_pf = str(player_season_stat[6] + player_career_stat[6])
		self.player_fg = str(player_season_stat[7] + player_career_stat[7])
		self.player_fgp = str(fgp)
		self.player_ftp = str(ftp)
		self.player_tpp = str(tpp)
		self.player_ft = str(player_season_stat[8] + player_career_stat[8])
		self.player_tp = str(player_season_stat[9] + player_career_stat[9])
			

def createNBATransactions(season):
	"""
	Creates a list a NBAPlayers Content Transactions by 
	converting each document in the NBAPlayers
	collection and converting it to a transaction object.
	"""

	NBATransactions = []

	player_id = []
		
	f2 = open('player_playoffs.txt')
	csv_f2 = csv.reader(f2)

	for row in csv_f2:
		if (row[1] == season) and (row[0] not in player_id):
			player_id.append(row[0])

	f2.close()			

	f1 = open('player_regular_season.txt')
	csv_f1 = csv.reader(f1)

	for row in csv_f1:
		if (row[1] == season) and (row[0] not in player_id):
			player_id.append(row[0])

	f1.close()	

	if player_id:
		for player in player_id:		
			NBADataTransaction = NBATransaction()
			NBADataTransaction.convertNBAContent(season, player)
			NBATransactions.append(NBADataTransaction)
		
	return NBATransactions


def convertToTransactions():
	"""
	Converts the NBAPlayers content into transactions and dumps into CSV
	in specified directory.
	"""
	NBASeasons = ['1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004']

	for season in NBASeasons:
		Transactions = []
		Transactions.extend(createNBATransactions(season))

		with open(season + '.csv','wb') as fp:
			writer = csv.writer(fp, delimiter=',')
			writer.writerow(["Season", "Player", "player_pts", "player_reb", "player_asts", "player_stl", "player_blk", "player_turnover", "player_pf", "player_fg", "player_ft", "player_tp", "player_fgp", "player_ftp", "player_tpp"])

			for transaction in Transactions:
				writer.writerow([transaction.Season, transaction.Player, transaction.player_pts, transaction.player_reb, transaction.player_asts, transaction.player_stl, transaction.player_blk, transaction.player_turnover, transaction.player_pf, transaction.player_fg, transaction.player_ft, transaction.player_tp, transaction.player_fgp, transaction.player_ftp, transaction.player_tpp])

	return Transactions

convertToTransactions()
