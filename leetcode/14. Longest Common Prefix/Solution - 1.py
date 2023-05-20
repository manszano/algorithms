#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return strs[0]
        prefix = strs[0]
        for i in range(len(prefix)):
            for stri in strs[1:]:
                if i == len(stri) or prefix[i] != stri[i]:
                    return prefix[0:i]
                    break
        return prefix


