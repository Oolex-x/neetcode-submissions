class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        result = 0

        for j, num in enumerate(sorted_nums):
            helper = []
            helper.append(num)
            index = 0
            for i in range(j+1, len(nums)):
                if sorted_nums[i] == (helper[index] + 1):
                    helper.append(sorted_nums[i])
                    index += 1
            if len(helper) > result:
                result = len(helper)


        return result