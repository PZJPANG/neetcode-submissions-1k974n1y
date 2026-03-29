class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocount = 0
        prod = 1
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zerocount += 1
        if zerocount > 1:
            return [0] * len(nums)
        elif zerocount == 1:
            ans = [0] * len(nums)
            for i, num in enumerate(nums):
                if num == 0:
                    ans[i] = prod
                    return ans
        else:
            ans = [0] * len(nums)
            for i, num in enumerate(nums):
                ans[i] = prod // num
            return ans 
                    
            
            