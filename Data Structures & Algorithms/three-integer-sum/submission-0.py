class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + num > 0:
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans