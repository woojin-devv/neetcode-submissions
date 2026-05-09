from collections import Counter as c

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fq = c(nums).most_common(k)
        return [num for num, _ in fq]
        