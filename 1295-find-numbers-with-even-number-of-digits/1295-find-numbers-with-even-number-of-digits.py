class Solution(object):
    def findNumbers(self, nums):
        count_even = 0
        for i in nums:
            count=0
            while i>0:
                i=i//10
                count=count+1
            if  count%2==0:
                count_even=count_even+1
        return count_even
           
        