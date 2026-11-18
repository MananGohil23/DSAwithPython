class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        counts = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                counts.append(count)
                count = 0
        counts.append(count)
        return max(counts)
        