print("menu")
print("3 - level 3")
print("4 - level 4")

examlevel = int(input("Enter Exam Level: "))

if examlevel == 3:
    mark = int(input("Enter Level 3 mark: "))
    if mark >= 65:
        print("pass")
    else:
        print("fail")

if examlevel == 4:
    mark = int(input("enter level 4 mark: "))
    if mark >=50:
        print("PASS")
    else:
        print("fail")
else:
    print("invalid choice")
