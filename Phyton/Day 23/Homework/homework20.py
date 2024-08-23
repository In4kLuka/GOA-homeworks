def manual_string(str):
    if str.find("u") % 2 == 0:
        return str.upper()
    else:
        return str.capitalize()
print(manual_string("luka"))