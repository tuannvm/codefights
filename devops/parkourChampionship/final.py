import os
dataDict = []
counter = 1
maxNum = 0
DIR='root/devops/teams/'
teams=os.listdir(DIR)
for team in teams:
    teamDir=DIR + team
    players=os.listdir(teamDir)
    playerList = []
    total = 0
    for player in players:
        playerList.append(player.rsplit( ".", 1 )[0])
        playerFile=DIR + team + '/' + player      
        with open(playerFile,'r') as f:
            data = f.readlines()
        for line in data:
            element = line.split()
            for i in range(0,len(element)):
                total = total + int(element[i])
    dataDict.append({'team': int(team), 'total': total, 'players': sorted(playerList)})
    #dataDict[team] = [total,sorted(playerList)]

dataDict =  sorted(dataDict,key=lambda k: k['team'], reverse=False)
dataDict =  sorted(dataDict,key=lambda k: k['total'], reverse=True)
for i in range(0, len(dataDict)):
    print str(i+1) + '. ' + ', '.join(dataDict[i]['players']) + ' - ' + str(dataDict[i]['total'])
#print sorted (dataDict.iteritems(), key=lambda (k,v): (v,k))

#while counter < len(dataDict):
#    for key, value in dataDict.iteritems():
        
#        print str(counter)  + '. ' + ', '.join(value[1]) + ' - ' + str(value[0])
#        counter = counter + 1
print dataDict