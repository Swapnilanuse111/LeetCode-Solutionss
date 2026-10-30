class Solution:
    def removeDuplicates(self, nums: list[int]):
        slow=0
        for fast in range(1,len(nums)):
            if nums[slow]!=nums[fast]:
                slow=slow+1
                nums[slow]=nums[fast]
        return slow+1


        