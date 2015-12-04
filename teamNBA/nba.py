#!/usr/bin/env python
"""
nba_team.py
:Author: Abhinandan Kelgere Ramesh
:Date: 11/10/2015
This module defines NBA team_season class that aggregates 
the data from all the NBA team_season collections and wraps it up in 
to a transactional format.
"""

import csv

import sys
reload(sys)


class NBATransaction:
	"""
	This class consists of a transaction object corresponding to 
	the NBA team_season data.This class object represents the data aggregated 
	over all the NBA team_season collections and combined to a single class.
	Collection: 
	------------------------------------------------------------------------------
	team_season
	------------------------------------------------------------------------------
	"""
	def __init__(self):
		self.Team = "None"
		self.Season = "None"
		self.team_o_fgm = "0"
		self.team_o_fga = "0"
		self.team_o_ftm = "0"
		self.team_o_fta = "0"
		self.team_o_oreb = "0"
		self.team_o_dreb = "0"
		self.team_o_reb = "0"
		self.team_o_asts = "0"
		self.team_o_pf = "0"
		self.team_o_stl = "0"
		self.team_o_to = "0"
		self.team_o_blk = "0"
		self.team_o_3pm = "0"
		self.team_o_pts = "0"
		self.team_d_fgm = "0"
		self.team_d_fga = "0"
		self.team_d_ftm = "0"
		self.team_d_fta = "0"
		self.team_d_oreb = "0"
		self.team_d_dreb = "0"
		self.team_d_reb = "0"
		self.team_d_asts = "0"
		self.team_d_pf = "0"
		self.team_d_stl = "0"
		self.team_d_to = "0"
		self.team_d_blk = "0"
		self.team_d_3pm = "0"
		self.team_d_pts = "0"
		self.team_pace = "0"
		self.prev_winrate = "0"
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
		self.coach_season_win_rate = "0"
		self.coach_career_win_rate = "0"
		self.win_rate = "0"
		self.Class = "0"

		
	def __str__(self):
		return "Team: %s , Season: %s , team_o_fgm: %s , team_o_fga: %s , team_o_ftm: %s , team_o_fta: %s , team_o_oreb: %s , team_o_dreb: %s , team_o_reb: %s, team_o_asts: %s , team_o_pf: %s , team_o_stl: %s , team_o_to: %s , team_o_blk: %s , team_o_3pm: %s , team_o_pts: %s , team_d_fgm: %s , team_d_fga: %s , team_d_ftm: %s , team_d_fta: %s , team_d_oreb: %s , team_d_dreb: %s , team_d_reb: %s, team_d_asts: %s , team_d_pf: %s , team_d_stl: %s , team_d_to: %s , team_d_blk: %s , team_d_3pm: %s , team_d_pts: %s , team_pace: %s , prev_winrate: %s , season_gp: %s, season_minutes: %s, season_pts: %s, season_dreb: %s, season_oreb: %s, season_reb: %s, season_asts: %s, season_stl: %s, season_blk: %s, season_turnover: %s, season_pf: %s, season_fga: %s, season_fgm: %s, season_fta: %s, season_ftm: %s, season_tpa: %s, season_tpm: %s, career_gp: %s, career_minutes: %s, career_pts: %s, career_dreb: %s, career_oreb: %s, career_reb: %s, career_asts: %s, career_stl: %s, career_blk: %s, career_turnover: %s, career_pf: %s, career_fga: %s, career_fgm: %s, career_fta: %s, career_ftm: %s, career_tpa: %s, career_tpm: %s , coach_season_win_rate: %s, coach_career_win_rate: %s, win_rate: %s , Class: %s" % (self.Team, self.Season, self.team_o_fgm, self.team_o_fga, self.team_o_ftm, self.team_o_fta, self.team_o_oreb, self.team_o_dreb, self.team_o_reb, self.team_o_asts, self.team_o_pf, self.team_o_stl, self.team_o_to, self.team_o_blk, self.team_o_3pm, self.team_o_pts, self.team_d_fgm, self.team_d_fga, self.team_d_ftm, self.team_d_fta, self.team_d_oreb, self.team_d_dreb, self.team_d_reb, self.team_d_asts, self.team_d_pf, self.team_d_stl, self.team_d_to, self.team_d_blk, self.team_d_3pm, self.team_d_pts, self.team_pace, self.prev_winrate, self.season_gp, self.season_minutes, self.season_pts, self.season_dreb, self.season_oreb, self.season_reb, self.season_asts, self.season_stl, self.season_blk, self.season_turnover, self.season_pf, self.season_fga, self.season_fgm, self.season_fta, self.season_ftm, self.season_tpa, self.season_tpm, self.career_gp, self.career_minutes, self.career_pts, self.career_dreb, self.career_oreb, self.career_reb, self.career_asts, self.career_stl, self.career_blk, self.career_turnover, self.career_pf, self.career_fga, self.career_fgm, self.career_fta, self.career_ftm, self.career_tpa, self.career_tpm, self.coach_season_win_rate, self.coach_career_win_rate, self.win_rate, self.Class)

	def __repr__(self):
		return "Team: %s , Season: %s , team_o_fgm: %s , team_o_fga: %s , team_o_ftm: %s , team_o_fta: %s , team_o_oreb: %s , team_o_dreb: %s , team_o_reb: %s, team_o_asts: %s , team_o_pf: %s , team_o_stl: %s , team_o_to: %s , team_o_blk: %s , team_o_3pm: %s , team_o_pts: %s , team_d_fgm: %s , team_d_fga: %s , team_d_ftm: %s , team_d_fta: %s , team_d_oreb: %s , team_d_dreb: %s , team_d_reb: %s, team_d_asts: %s , team_d_pf: %s , team_d_stl: %s , team_d_to: %s , team_d_blk: %s , team_d_3pm: %s , team_d_pts: %s , team_pace: %s , prev_winrate: %s , season_gp: %s, season_minutes: %s, season_pts: %s, season_dreb: %s, season_oreb: %s, season_reb: %s, season_asts: %s, season_stl: %s, season_blk: %s, season_turnover: %s, season_pf: %s, season_fga: %s, season_fgm: %s, season_fta: %s, season_ftm: %s, season_tpa: %s, season_tpm: %s, career_gp: %s, career_minutes: %s, career_pts: %s, career_dreb: %s, career_oreb: %s, career_reb: %s, career_asts: %s, career_stl: %s, career_blk: %s, career_turnover: %s, career_pf: %s, career_fga: %s, career_fgm: %s, career_fta: %s, career_ftm: %s, career_tpa: %s, career_tpm: %s , coach_season_win_rate: %s, coach_career_win_rate: %s, win_rate: %s , Class: %s" % (self.Team, self.Season, self.team_o_fgm, self.team_o_fga, self.team_o_ftm, self.team_o_fta, self.team_o_oreb, self.team_o_dreb, self.team_o_reb, self.team_o_asts, self.team_o_pf, self.team_o_stl, self.team_o_to, self.team_o_blk, self.team_o_3pm, self.team_o_pts, self.team_d_fgm, self.team_d_fga, self.team_d_ftm, self.team_d_fta, self.team_d_oreb, self.team_d_dreb, self.team_d_reb, self.team_d_asts, self.team_d_pf, self.team_d_stl, self.team_d_to, self.team_d_blk, self.team_d_3pm, self.team_d_pts, self.team_pace, self.prev_winrate, self.season_gp, self.season_minutes, self.season_pts, self.season_dreb, self.season_oreb, self.season_reb, self.season_asts, self.season_stl, self.season_blk, self.season_turnover, self.season_pf, self.season_fga, self.season_fgm, self.season_fta, self.season_ftm, self.season_tpa, self.season_tpm, self.career_gp, self.career_minutes, self.career_pts, self.career_dreb, self.career_oreb, self.career_reb, self.career_asts, self.career_stl, self.career_blk, self.career_turnover, self.career_pf, self.career_fga, self.career_fgm, self.career_fta, self.career_ftm, self.career_tpa, self.career_tpm, self.coach_season_win_rate, self.coach_career_win_rate, self.win_rate, self.Class)

	def convertNBAContent(self, team, player, coach):
		"""
		Converts the data in content into
		the transactional format and returns a NBA team_season
		Content transaction object.
		"""

		self.Team = team[0]
		self.Season = team[1]
		self.team_o_fgm = team[2]
		self.team_o_fga = team[3]
		self.team_o_ftm = team[4]
		self.team_o_fta = team[5]
		self.team_o_oreb = team[6]
		self.team_o_dreb = team[7]
		self.team_o_reb = team[8]
		self.team_o_asts = team[9]
		self.team_o_pf = team[10]
		self.team_o_stl = team[11]
		self.team_o_to = team[12]
		self.team_o_blk = team[13]
		self.team_o_3pm = team[14]
		self.team_o_pts = team[15]
		self.team_d_fgm = team[16]
		self.team_d_fga = team[17]
		self.team_d_ftm = team[18]
		self.team_d_fta = team[19]
		self.team_d_oreb = team[20]
		self.team_d_dreb = team[21]
		self.team_d_reb = team[22]
		self.team_d_asts = team[23]
		self.team_d_pf = team[24]
		self.team_d_stl = team[25]
		self.team_d_to = team[26]
		self.team_d_blk = team[27]
		self.team_d_3pm = team[28]
		self.team_d_pts = team[29]
		self.team_pace = team[30]
		self.prev_winrate = team[31]
		self.season_gp = player[2]
		self.season_minutes = player[3]
		self.season_pts = player[4]
		self.season_dreb = player[5]
		self.season_oreb = player[6]
		self.season_reb = player[7]
		self.season_asts = player[8]
		self.season_stl = player[9]
		self.season_blk = player[10]
		self.season_turnover = player[11]
		self.season_pf = player[12]
		self.season_fga = player[13]
		self.season_fgm = player[14]
		self.season_fta = player[15]
		self.season_ftm = player[16]
		self.season_tpa = player[17]
		self.season_tpm = player[18]
		self.career_gp = player[19]
		self.career_minutes = player[20]
		self.career_pts = player[21]
		self.career_dreb = player[22]
		self.career_oreb = player[23]
		self.career_reb = player[24]
		self.career_asts = player[25]
		self.career_stl = player[26]
		self.career_blk = player[27]
		self.career_turnover = player[28]
		self.career_pf = player[29]
		self.career_fga = player[30]
		self.career_fgm = player[31]
		self.career_fta = player[32]
		self.career_ftm = player[33]
		self.career_tpa = player[34]
		self.career_tpm = player[35]
		self.coach_season_win_rate = coach[2]
		self.coach_career_win_rate = coach[3]
		self.win_rate = team[32]
		self.Class = team[33]

		

def createNBATransactions():
	"""
	Creates a list of NBA team_season Transactions by 
	converting each document in the NBA team_season
	collection and converting it to a transaction object.
	"""

	NBATransactions = []
	
	NBATeams = ['ATL','BOS','CHI','CHA','CLE','DAL','DEN','DET','GSW','HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NJN', 'NOH', 'NYK', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'SEA', 'TOR', 'UTA', 'WAS']

	NBASeasons = ['1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004']

	for team in NBATeams:
		for season in NBASeasons:
			f = open('NBATeamTransactions.csv')
	 		csv_f = csv.reader(f)

	 		for row in csv_f:
    				if row[0] == team and row[1] == season:
					f1 = open('NBAPlayerTransactions.csv')
					csv_f1 = csv.reader(f1)
					for player in csv_f1:
						if player[0] == team and player[1] == season:
							f2 = open('NBAcoachTransactions.csv')
							csv_f2 = csv.reader(f2)
							for coach in csv_f2:
								if coach[0] == team and coach[1] == season:
									NBADataTransaction = NBATransaction()
									NBADataTransaction.convertNBAContent(row, player, coach)
									NBATransactions.append(NBADataTransaction)
									f2.close()
									break
							f1.close()
							break
					f.close()
					break

			f.close()

	return NBATransactions


def convertToTransactions():
	"""
	Converts the NBA team_season content into transactions and dumps into CSV
	in specified directory.
	"""
	Transactions = []
	Transactions.extend(createNBATransactions())

	with open('NBATransactions.csv','wb') as fp:
		writer = csv.writer(fp, delimiter=',')
		writer.writerow(["Team", "Season", "team_o_fgm", "team_o_fga", "team_o_ftm", "team_o_fta", "team_o_oreb", "team_o_dreb", "team_o_reb", "team_o_asts", "team_o_pf", "team_o_stl", "team_o_to", "team_o_blk", "team_o_3pm", "team_o_pts", "team_d_fgm", "team_d_fga", "team_d_ftm", "team_d_fta", "team_d_oreb", "team_d_dreb", "team_d_reb", "team_d_asts", "team_d_pf", "team_d_stl", "team_d_to", "team_d_blk", "team_d_3pm", "team_d_pts", "team_pace", "prev_winrate", "player_season_gp", "player_season_minutes", "player_season_pts", "player_season_dreb", "player_season_oreb", "player_season_reb", "player_season_asts", "player_season_stl", "player_season_blk", "player_season_turnover", "player_season_pf", "player_season_fga", "player_season_fgm", "player_season_fta", "player_season_ftm", "player_season_tpa", "player_season_tpm", "player_career_gp", "player_career_minutes", "player_career_pts", "player_career_dreb", "player_career_oreb", "player_career_reb", "player_career_asts", "player_career_stl", "player_career_blk", "player_career_turnover", "player_career_pf", "player_career_fga", "player_career_fgm", "player_career_fta", "player_career_ftm", "player_career_tpa", "player_career_tpm", "coach_season_win_rate", "coach_career_win_rate", "win_rate", "Class"])

		for transaction in Transactions:
			writer.writerow([transaction.Team, transaction.Season, transaction.team_o_fgm, transaction.team_o_fga, transaction.team_o_ftm, transaction.team_o_fta, transaction.team_o_oreb, transaction.team_o_dreb, transaction.team_o_reb, transaction.team_o_asts, transaction.team_o_pf, transaction.team_o_stl, transaction.team_o_to, transaction.team_o_blk, transaction.team_o_3pm, transaction.team_o_pts, transaction.team_d_fgm, transaction.team_d_fga, transaction.team_d_ftm, transaction.team_d_fta, transaction.team_d_oreb, transaction.team_d_dreb, transaction.team_d_reb, transaction.team_d_asts, transaction.team_d_pf, transaction.team_d_stl, transaction.team_d_to, transaction.team_d_blk, transaction.team_d_3pm, transaction.team_d_pts, transaction.team_pace, transaction.prev_winrate, transaction.season_gp, transaction.season_minutes, transaction.season_pts, transaction.season_dreb, transaction.season_oreb, transaction.season_reb, transaction.season_asts, transaction.season_stl, transaction.season_blk, transaction.season_turnover, transaction.season_pf, transaction.season_fga, transaction.season_fgm, transaction.season_fta, transaction.season_ftm, transaction.season_tpa, transaction.season_tpm, transaction.career_gp, transaction.career_minutes, transaction.career_pts, transaction.career_dreb, transaction.career_oreb, transaction.career_reb, transaction.career_asts, transaction.career_stl, transaction.career_blk, transaction.career_turnover, transaction.career_pf, transaction.career_fga, transaction.career_fgm, transaction.career_fta, transaction.career_ftm, transaction.career_tpa, transaction.career_tpm, transaction.coach_season_win_rate, transaction.coach_career_win_rate, transaction.win_rate, transaction.Class])

	return Transactions

convertToTransactions()
