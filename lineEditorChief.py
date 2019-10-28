sn = open("filename.txt", "r+")
sn2 = "this is a new line\n"
sn2+= sn.read()
sn.write(sn2)
sn.close()
    
