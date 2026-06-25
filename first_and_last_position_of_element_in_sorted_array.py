class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] == target:
                result.append(i)

        if result == []:
            return [-1 , -1]
        
        for i in range(n):
            if result == [i]:
                return [i , i]
        
        
        return [min(result) , max(result)]