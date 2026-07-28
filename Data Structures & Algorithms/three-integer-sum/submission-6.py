class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for index in range(len(nums)): 

            if index > 0 and nums[index - 1] == nums[index]:
                continue

            i = index + 1
            j = len(nums) - 1
            num = nums[index]
            while i < j:
                if num + nums[i] + nums[j] > 0:
                    j -= 1
                elif num + nums[i] + nums[j] < 0:
                    i += 1
                else:
                    result.append([num, nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
            

        return result