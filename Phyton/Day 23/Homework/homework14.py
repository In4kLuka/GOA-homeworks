def names_list(names):
    uppercase_names = []
    for i in names:
        uppercase_names.append(i[0].upper() + i[1::])
    return uppercase_names
print(names_list(["luka", "nika", "lasha", "malxazi"]))