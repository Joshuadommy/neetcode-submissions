class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        
        for num in nums:
            if num in h:
                return True
            h[num] = h.get(num, 0) + 1

        return False