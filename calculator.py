number1 = int(input("enter a number:"))
number2 = int(input("enter another number:"))
sign = input("enter a sign:")

if sign == "+":
    print(number1+number2)
elif sign == "-":
      print(number1-number2)
elif sign == "*":
    print(number1*number2)
elif sign == "/":
    print(number1/number2)
elif sign == "**":
    print(number1**number2)
elif sign == "//":
    print(number1//number2)
elif sign == "%":
    print(number1%number2)
else: print("invalid error!")