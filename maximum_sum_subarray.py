class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        answer = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0

            currSum += nums[i]

            if currSum > answer:
                answer = currSum

        return answer