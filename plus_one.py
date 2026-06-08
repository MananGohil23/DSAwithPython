class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        number = 0
        sol = []
        for i in range(n+1):
            pow = n-i
            dig = digits[i]*(10**pow)     
            number += dig
        result = str(number +1)

        for i in range(len(result)):
            sol.append(int(result[i]))
        return sol
        