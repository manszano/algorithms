
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
#Given a Roman number(s) return the roman number as integer
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: romans[x], s))