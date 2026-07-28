class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # must sum to 0, 3 unique indexes
        
        result = []
        


        nums = sorted(nums)

        for index, num in enumerate(nums): 
            i = index + 1
            j = len(nums) - 1
            while i < j:
                if num + nums[i] + nums[j] == 0 and not [num, nums[i], nums[j]] in result :
                    result.append([num, nums[i], nums[j]])
                if num + nums[i] + nums[j] > 0:
                    j -= 1
                    continue
                if num + nums[i] + nums[j] < 0:
                    i += 1
                    continue
                j -= 1
                i += 1
            

        return result