class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for k in range(1,len(arr)):
            if k < len(arr) - 1 and arr[k] - arr[k + 1] != arr[0] - arr[1]:
                return False
        return True