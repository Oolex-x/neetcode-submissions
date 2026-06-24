class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        amt = k
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        sortedFreq = sorted(frequency.items(), key = lambda x: x[1])

        for key,value in reversed(sortedFreq):
            if amt > 0:
                result.append(key)
                amt -=1
            else:
                break

        return result

