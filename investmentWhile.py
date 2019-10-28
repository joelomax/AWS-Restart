inv = 100
yearcount = 0

while inv <= 1000:
    inv = inv + (inv/10)
    yearcount+=1

print("your investment will take", yearcount, "years to reach £1000")
