num1 = int(input("first number: "))
num2 = int(input("second number: "))
operator = str(input("operator: "))


if operator == "-":
    if num2 > num1:
        minus = num2 - num1
        print("-", minus)
              
elif operator == "x" or "X" or "*":
    print(num1 * num2)

elif operator == "+":
    print(num1 + num2)

elif operator == "/" or "divide":
    print(num1/num2)

else:
    print("invalid operator")

