class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        temp = nums.copy()
        nums[k::] = temp[:len(nums)-k]
        nums[:k] = temp[len(nums)-k:]
        