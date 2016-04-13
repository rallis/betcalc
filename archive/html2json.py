#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,re,json
import requests, urllib,urllib2
from bs4 import BeautifulSoup

jsonData = {}
jsonData['sport'] = 'soccer'
jsonData['stats'] = []
lastTimestamp = -1

fileMin =1
fileMax =350 
# every 20sec, 3/min, 90+15+10=115*3=345 <350

for fileInd in xrange(fileMin, fileMax+1):
	print fileInd
	
	try:
		fin =open(str(fileInd)+".html", "r")
	except IOError:
		print "CANNOT OPEN FILE ["+str(fileInd)+"]"
	else:
		soup = BeautifulSoup(fin.read(), "html.parser")
		navbar = soup.find("div", {"class": "ml1-ScoreHeader "})
		if navbar==None: 1/0

		teamA = navbar.contents[0].contents[0].contents[0].text
		teamAscore = navbar.contents[0].contents[0].contents[1].text

		teamB = navbar.contents[1].contents[0].contents[1].text
		teamBscore = navbar.contents[1].contents[0].contents[0].text

		timestamp = navbar.contents[2].text
		[minutes, seconds] = map(int,timestamp.split(':'))
		#print minutes,seconds,60*minutes + seconds
		if lastTimestamp <0 : lastTimestamp = 60*minutes + seconds - 1
		if lastTimestamp <= 60*minutes + seconds:
			lastTimestamp = 60*minutes + seconds
			#print [timestamp, teamA, teamAscore, teamB, teamBscore]
			#fout.write("###\n###"+timestamp +'--'+ teamA +'--'+ teamAscore +'--'+ teamB +'--'+ teamBscore+"\n###\n")
			jsonData['teamA'] = teamA
			jsonData['teamB'] = teamB
			curStat = {'timestamp': timestamp, 'scoreA': teamAscore, 'scoreB': teamBscore, 'bets':{}}
			# curStat['file'] = fileInd
			# curStat['lastTimestamp'] = lastTimestamp

			markets = soup.find("div", {"id": "MarketGrid"})
			for i in range(len(markets.contents)):
				marketTitle = markets.contents[i].contents[0].text
				#fout.write('##'+str(marketTitle)+"\n")
				curStat['bets'][marketTitle]={}

				marketData = markets.contents[i].find("div", {"class": "ipe-MarketContainer"})
				#print marketData
				if marketData!=None:
					marketDetails = marketData.find_all("div", {"class": "ipe-Participant"})
					#print marketDetails
					for betMarket in marketDetails:
						betOption = betMarket.find("span", {"class": "ipe-Participant_OppName"}).text
						betOdds = betMarket.find("span", {"class": "ipe-Participant_OppOdds"}).text
						#fout.write(str(betOption)+" # "+str(betOdds)+"\n")
						curStat['bets'][marketTitle][betOption] = betOdds

			jsonData['stats'].append(curStat)			


#print jsonData
fout = open(teamA+'___'+teamB+'.txt',"w")
json.dump(jsonData, fout)
fout.close()

