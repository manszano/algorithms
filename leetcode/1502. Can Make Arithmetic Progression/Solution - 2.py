class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()
        a = arr[0] - arr[1]
        for k in range(len(arr)):
            if k < len(arr) - 1:
                if arr[k] - arr[k + 1] != a:
                    return False

        return True