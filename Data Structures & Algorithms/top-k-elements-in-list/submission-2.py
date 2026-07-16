class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []

        for num in nums:
            frequency[num] = frequency.get(num,0) + 1
        print(frequency)

        for key, value in sorted(frequency.items(), key = lambda x: x[1], reverse = True):
            if k > 0:
                result.append(key)
                k -= 1
            else:
                break

        return result