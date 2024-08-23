def manual_list(str):
    new_list = []
    for i in str:
        if len(i) % 2 == 0:
            new_list.append(i.upper())
        else:
            new_list.append(i[0].upper() + i[1::].lower())
    return new_list
print(manual_list(["luka", "anton", "nika", "funqcia"]))
