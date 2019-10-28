def product(listofNumbers):
    total = 1
    for individualNumber in listofNumbers:
       total *= individualNumber
    return total

print(product([4,5,5]))
