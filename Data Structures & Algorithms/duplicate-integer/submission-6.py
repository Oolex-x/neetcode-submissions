class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     nums_size = len(nums)
     if len(set(nums)) < nums_size:
         return True
     return False 