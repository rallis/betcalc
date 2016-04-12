#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,re
import requests, urllib,urllib2
from bs4 import BeautifulSoup

fout = open("output.txt","w")
fileMin =1
fileMax =131

for fileInd in xrange(fileMin, fileMax+1):
	print fileInd
	fin =open(str(fileInd)+".html", "r")
	soup = BeautifulSoup(fin.read(), "html.parser")

	navbar = soup.find("div", {"class": "ml1-ScoreHeader "})

	if navbar==None: 1/0

	teamA = navbar.contents[0].contents[0].contents[0].text
	teamAscore = navbar.contents[0].contents[0].contents[1].text

	teamB = navbar.contents[1].contents[0].contents[1].text
	teamBscore = navbar.contents[1].contents[0].contents[0].text

	timestamp = navbar.contents[2].text
	#print [timestamp, teamA, teamAscore, teamB, teamBscore]
	fout.write("###\n###"+timestamp +'--'+ teamA +'--'+ teamAscore +'--'+ teamB +'--'+ teamBscore+"\n###\n")

	markets = soup.find("div", {"id": "MarketGrid"})
	for i in range(len(markets.contents)):
		marketTitle = markets.contents[i].contents[0].text
		fout.write('##'+str(marketTitle)+"\n")

		marketData = markets.contents[i].find("div", {"class": "ipe-MarketContainer"})
		#print marketData
		marketDetails = marketData.find_all("div", {"class": "ipe-Participant"})
		#print marketDetails
		for betMarket in marketDetails:
			betOption = betMarket.find("span", {"class": "ipe-Participant_OppName"}).text
			betOdds = betMarket.find("span", {"class": "ipe-Participant_OppOdds"}).text
			fout.write(str(betOption)+" # "+str(betOdds)+"\n")


fout.close()

#r = requests.get(root+curLink, verify=False)
#r.encoding="utf-8"
#content = soup.find("div", {"id": "rt-main"})
#tmpLinks = soup.find_all('a')
#print tmpLinks

	#print i, markets.contents[i].text, len(markets.contents[i])
	# for j in range(1,len(markets.contents[i])):
	# 	print "\t",j,  markets.contents[i].contents[j]
	# 	#if len(markets.contents[i].contents[j])>0:
		#	print markets.contents[i].contents[j].contents[0]
