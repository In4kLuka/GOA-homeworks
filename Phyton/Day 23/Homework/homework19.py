def manual_list(string):
    new_list = []
    for i in string:
        if i.isupper():
            new_list.append(i.lower())
        elif i.islower():
            new_list.append(i.upper())
    return new_list
print(manual_list(["LUKA", "nika", "saba", "DATO"]))