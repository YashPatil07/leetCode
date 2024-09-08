class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue 
                    
            hashmap=set()
            
            for j in range(i+1,len(nums)):
                third = -(nums[i]+nums[j])
                # rem = target - third
                if third in hashmap:    
                    temp =[nums[i],nums[j],third]
                    st.add(tuple(temp))
                hashmap.add(nums[j])             
                
        ans = list(st)
        return ans
