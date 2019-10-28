file = open("sportTeamGo.txt", "r")

file.readline()
file.readline()
file.seek(2)
print(file.read())
file.seek(3)
print(file.read())
file.close()
