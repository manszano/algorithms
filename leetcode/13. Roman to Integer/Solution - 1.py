
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
#Given a Roman number(s) return the roman number as integer
class Solution:
    def romanToInt(self, s: str) -> int:


        def roman1(roman):
            value = 0
            if roman == "M":
                value += 1000
            elif roman == "D":
                value += 500
            elif roman == "C":
                value += 100
            elif roman == "L":
                value += 50
            elif roman == "X":
                value += 10
            elif roman == "V":
                value += 5
            elif roman == "I":
                value += 1
            return value


        lista = list(s)
        value2 = list(map(roman1, lista))
        result = 0
        i = len(value2) - 1
        while i >= 0:
            if value2[i - 1] < value2[i] and i > 0:
                result += value2[i] - value2[i - 1]
                i -= 1
            else:
                result += value2[i]
            i -= 1
        return result