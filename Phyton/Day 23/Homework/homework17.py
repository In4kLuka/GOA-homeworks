def manual_list(string):
    odd = [] #kenti
    even = [] #luwi
    for i in string:
        if len(i) % 2 == 0:
            even.append(i.upper())
        else:
            odd.append(i.upper())
    print(odd)
    print(even)
manual_list(["luka", "anton", "nika", "funqcia"])