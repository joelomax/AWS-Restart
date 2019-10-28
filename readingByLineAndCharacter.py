file = open("filename.txt", "r")

print("first line: ")
print(file.readline())
file.seek(1)
print("first character: ")
print(file.read(1))
file.readline()
print("second line: ")
print(file.readline())

print(file.read(2))
file.close()
