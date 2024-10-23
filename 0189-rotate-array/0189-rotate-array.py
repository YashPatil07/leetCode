class Solution:
    def rotate(self, nums, k):
        # Create a temporary list to hold the rotated elements
        temp = [0] * len(nums)
        
        # Rotate elements
        for i in range(len(nums)):
            # print(f"(i+k): {i+k}, len(nums): {len(nums)}, (i+k)%len(nums): {(i+k) % len(nums)}")
            temp[(i + k) % len(nums)] = nums[i]
        
        # Copy the rotated elements back into the original list
        nums[:] = temp