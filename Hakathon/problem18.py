def calculator():
    num1 = int(input("please enter number 1: "))
    num2 = int(input("please enter number 2: "))
    op = input("please enter math operator(+, -, *, /): ")
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("IT IS NOT A MATH OPERATOR")
calculator()
