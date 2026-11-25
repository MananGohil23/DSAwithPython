class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while n>1:
            for i in range(1,n):
                if nums[i]<nums[i-1]:
                    nums[i] , nums[i-1] = nums[i-1], nums[i]
            n-=1
        