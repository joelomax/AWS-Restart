coolFile = open("sportTeamGo.txt", "w")
teamNames = ["redTheReds", "teamGoGoSportas", "teamkickadaball", "wotDoIPutHere", "crochetpadewans"]
numTeams = 0
while numTeams < 6:
    coolFile.write(teamNames[numTeams] + "\n")
    numTeams+=1

coolFile.close()
coolFile = open("sportTeamGo.txt", "r")

print("first team is ", coolFile.readline())
print("second team is ", coolFile.readline())

coolFile.close()
