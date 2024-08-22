def palindrome(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        print(True)
    else:
        print(False)
palindrome("wow")  