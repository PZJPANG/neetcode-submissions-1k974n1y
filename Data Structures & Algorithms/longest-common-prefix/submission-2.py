class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            if not word:
                return ""
            while word and prefix != word[:len(prefix)]:
                prefix = prefix[:len(prefix) - 1]
        return prefix