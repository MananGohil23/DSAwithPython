class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        num1 = []
        num2 = []
        for item in nums1:
            if item not in nums2 and item not in num1:
                num1.append(item)
                
        for item in nums2:
            if item not in nums1 and item not in num2:
                num2.append(item)
        answer.append(num1)
        answer.append(num2)
        return answer