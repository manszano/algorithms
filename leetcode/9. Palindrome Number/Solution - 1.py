#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:

    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        length = len(y) - 1
        reverse = ""
        while length >= 0:
            reverse += y[length]
            length -= 1

        if y == reverse:
            return True

        else:
            return False

