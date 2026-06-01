class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        dup_count = []
        i = 0
        while i < len(arr):
            count = 1
            while i+1 <len(arr) and arr[i] ==arr[i+1]:
                count = count  + 1
                i = i+1
            dup_count.append(count)
            i = i+1
        dup_count.sort()
        for i in range(1 , len(dup_count)):
            if dup_count[i] == dup_count[i-1]:
                return False
        
        return True