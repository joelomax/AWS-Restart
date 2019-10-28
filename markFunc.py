paper = int(input("choice of paper, please type: \n 1 for ICT Homework \n 2 for Assessment \n 3 for ICT Final Exam"))
if paper == 1:
    topmark = 25
elif paper == 2:
    topmark =50
elif paper == 3:
    topmark = 100
else:
    print("invalid input")
        
mark = int(input("mark: "))
if mark > topmark * 0.9:
    print("the score is A")
elif mark > topmark * 0.8:
    print("the score is B")
elif mark > topmark * 0.7:
    print("the score is C")
elif mark > topmark * 0.6:
    print("the score is D")
elif mark <= topmark * 0.6:
    print("the score is E")
else:
    print("invalid input")

percHW = mark
percAssess = 
percFinal =


        
