# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


def is_palindrome(s):
    return s == s[::-1]


ans = is_palindrome("malayalam")
if ans:
    print("Yes")
else:
    print("No")