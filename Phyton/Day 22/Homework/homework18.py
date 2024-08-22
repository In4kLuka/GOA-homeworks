def two_integers(num1, num2):
    lst1 = []
    lst2 = []
    maximum = 0
    for i in range(1,num1):
        if num1 % i == 0:
            lst1.append(i)
    for i in range(1,num2):
        if num2 % i == 0:
            lst2.append(i)
    if max(lst1) == max(lst2):
        print(max(lst1)) 
two_integers(