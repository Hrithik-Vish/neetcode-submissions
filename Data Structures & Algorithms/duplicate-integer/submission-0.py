class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        
        return len(set(nums)) != len(nums)