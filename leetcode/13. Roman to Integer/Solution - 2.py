
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
#Given a Roman number(s) return the roman number as integer
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and romans[s[i]] < romans[s[(i + 1)]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]
        return result