class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        num_sum = 0
        n = len(nums)
        for i in range(n+1):
            sum += i
        
        for num in nums:
            num_sum += num

        missing = sum - num_sum

        return missing
    