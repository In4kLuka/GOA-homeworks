def numbers(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
    return sum
print(numbers([1,2,3,4]))