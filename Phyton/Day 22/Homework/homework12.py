def my_string(str):
    sum = 0
    for i in str:
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
my_string("luka")