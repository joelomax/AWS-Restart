userword = str(input("enter a word: "))
vowelcount= 0
vowellist= ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for char in userword:
    if char in vowellist:
        vowelcount+=1
print("there are", vowelcount, "vowels in this word")
