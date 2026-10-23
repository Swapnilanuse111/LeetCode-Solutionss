
class Solution:
    def findTheDifference(self, s, t):
        s = sorted(s)
        t = sorted(t)

        left = 0

        while left < len(s):
            if s[left] != t[left]:
                return t[left]
            left += 1

        return t[left]
