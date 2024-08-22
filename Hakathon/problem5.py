sum = 0
string = input("please enter string: ")
for i in string:
    if i == "a":
        sum += 1
    elif i == "e":
        sum += 1
    elif i == "i":
        sum += 1
    elif i == "o":
        sum += 1
    elif i == "u":
        sum += 1 
    else:
        sum += 0
print(sum)