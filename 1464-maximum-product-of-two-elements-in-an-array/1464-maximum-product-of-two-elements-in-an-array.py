class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        largest = 0
        secondLargest = 0

        for i in nums:

            if i > largest:
                secondLargest = largest
                largest = i

            elif i > secondLargest:
                secondLargest = i

        return (largest - 1) * (secondLargest - 1)