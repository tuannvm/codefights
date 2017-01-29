#!/bin/bash
python << END
import os
dataDict = {}
counter = 1
DIR='root/devops/teams/'
teams=os.listdir(DIR)
for team in teams:
    teamDir=DIR + team
    players=os.listdir(teamDir)
    playerList = []
    total = 0
    for player in players:
        playerList.append(player.strip('.txt'))
        playerFile=DIR + team + '/' + player      
        with open(playerFile,'r') as f:
            data = f.readlines()
        for line in data:
            element = line.split()
            for i in range(0,len(element)):
                total = total + int(element[i])
    dataDict[team] = [total,sorted(playerList)]

sorted(dataDict.values())
for key, value in dataDict.iteritems():
    print str(counter)  + '. ' + ', '.join(value[1]) + ' - ' + str(value[0])
    counter = counter + 1
END