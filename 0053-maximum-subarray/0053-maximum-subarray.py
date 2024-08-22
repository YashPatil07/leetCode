class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')  # Initialize to the lowest possible value
        currentSum = 0  # This will store the sum of the current subarray
        
        for num in nums:
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0  # Reset the current sum if it goes negative
        
        return maxSum