class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
             valid = list()
             for i in range(len(nums)):
                for x in range(i+1,len(nums)):
                    if nums[i] + nums[x] == target:
                        valid.append(i)
                        valid.append(x)
                        return valid