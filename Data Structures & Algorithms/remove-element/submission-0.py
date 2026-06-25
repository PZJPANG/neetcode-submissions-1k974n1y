class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        i, j = 0, 0
        while i < k:
            while nums[j] == val:
                j += 1
            nums[i] = nums[j]
            i += 1
            j += 1
        return k


            