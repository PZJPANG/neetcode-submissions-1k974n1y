class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_num = {}
        ans = 0
        temp = 0
        for num in nums:
            seen_num[num] = 1 + seen_num.get(num, 0)
        for num in nums:
            if num - 1 not in seen_num:
                temp = 1
                while num + 1 in seen_num:
                    temp += 1
                    num += 1
                ans = max(ans, temp)
            else:
                pass
        return ans



                
