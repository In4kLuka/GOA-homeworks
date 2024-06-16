num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1 > num2:
    for i in range(num2,num1):
        print(i)
else:
    for i in range(num1,num2):
        print(i)        