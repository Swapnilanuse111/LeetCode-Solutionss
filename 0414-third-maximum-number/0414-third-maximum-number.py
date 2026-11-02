class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        largest=float('-inf')
        s_largest=float('-inf')
        t_largest=float('-inf')
        for i in nums:
            if i>largest:
                t_largest=s_largest
                s_largest=largest
                largest=i
            elif i>s_largest and i!=largest:
                t_largest=s_largest
                s_largest=i
            elif i>t_largest and i!=s_largest and i!=largest:
                t_largest=i
        if t_largest == float('-inf'):
            return largest
        return t_largest
        