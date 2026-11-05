class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[0]*len(nums)
        left=0
        right=len(nums)-1
        pos = len(nums) - 1
        while left<=right:
            
            if nums[left] ** 2 > nums[right] ** 2:
                ans[pos] = nums[left] ** 2
                left += 1
            else:
                ans[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return ans



        