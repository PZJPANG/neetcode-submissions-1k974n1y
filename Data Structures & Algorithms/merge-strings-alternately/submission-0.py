class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        ans = []
        while l < len(word1) or r < len(word2):
            if l == len(word1): 
                ans.append(word2[r::])
                break
            elif r == len(word2):
                ans.append(word1[l::])
                break
            ans.append(word1[l])
            ans.append(word2[r])
            l += 1
            r += 1
        return "".join(ans)
