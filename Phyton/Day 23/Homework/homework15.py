def manual_list(numbers):
    new_list = []
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i / 2)
        else:
            new_list.append(i * 2)
    return new_list
print(manual_list([1,2,3,4]))