class Solution:
    def canAliceWin(self, n: int) -> bool:
        start = 10
        if n < 10:
            return False
        while start > 0:
            n = n - start
            start -= 1 
            if start > n:
                if start%2==0:
                    return False
                else:
                    return True
