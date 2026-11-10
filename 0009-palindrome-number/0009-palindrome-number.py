class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False
        
        reverse_num = 0

        while x > reverse_num:
            digit = x % 10
            reverse_num = reverse_num * 10 + digit
            x = x // 10

        return x == reverse_num or x == reverse_num // 10

