class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        result = ''.join(char for char in s1 if char.isalnum())

        if result == result[::-1]:
            return True
        return False