from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = Counter(nums)
        num_to_freq = sorted(list(num_to_freq.items()), key=lambda x: x[1])
        return [num for num, _ in num_to_freq][-k:]