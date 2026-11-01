class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total=0
        ans=[]
        for i in nums:
            total=total+i
            ans.append(total)
        return ans