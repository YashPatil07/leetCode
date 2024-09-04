class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mapp = defaultdict(int)
        presum = 0
        cnt = 0
        mapp[0] = 1
        for i in range(n):
            
            presum += nums[i]
            rem = presum - k
            # add the number of subarrays to be removed:
            cnt +=mapp[rem]
            #update the count of prefix sum in the map
            mapp[presum] +=1
        return cnt  