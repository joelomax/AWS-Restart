file = open("filename.txt", "r")

print("First line: " + file.readline())
print("second line: " + file.readline())
print("rest of the file: " + file.read())
print("blank line: " + file.readline())

file.close()
