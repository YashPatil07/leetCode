class Solution:
    def merge(self, nums, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        
        # Merge both halves in sorted order
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        # Collect remaining elements from the left half
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        # Collect remaining elements from the right half
        while right <= high:
            temp.append(nums[right])
            right += 1
        
        # Copy back the merged elements into the original list
        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    def countPairs(self, nums, low, mid, high):
        count = 0
        right = mid + 1
        # Count the reverse pairs
        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            count += (right - (mid + 1))
        return count

    def mergeSort(self, nums, low, high):
        count = 0
        if low >= high:
            return count
        mid = (low + high) // 2
        count += self.mergeSort(nums, low, mid)
        count += self.mergeSort(nums, mid + 1, high)
        count += self.countPairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)
        return count

    def reversePairs(self, nums):
        if not nums:
            return 0
        return self.mergeSort(nums, 0, len(nums) - 1)
