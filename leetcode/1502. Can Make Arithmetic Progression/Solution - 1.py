
#A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

#Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

class Solution:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        for i in range(1,len(arr)):
            j = i - 1
            s = arr[i]
            while j >= 0 and s < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = s
                j -= 1

        a = arr[0] - arr[1]

        for k in range(len(arr)):
            if k < len(arr) - 1:
                if arr[k] - arr[k + 1] != a:
                    return False

        return True