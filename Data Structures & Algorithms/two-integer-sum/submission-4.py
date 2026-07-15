class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        i = 0
        for i in range(0,len(nums)):
            vals[i] = target - nums[i]
        print(vals)
        
        for key, value in vals.items():
            for i in range(key+1,len(nums)):
                if value == nums[i]:
                    ans = [key, i]
                    return ans


        return ans
