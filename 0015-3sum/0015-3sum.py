
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
             
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i]+nums[j]+nums[k]

                if total < 0:
                    j+=1
                elif total > 0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1 
                    
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
        return ans    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #time complexity and space complexity is o(n^2)
#         st = set()
#         nums.sort()
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i - 1]:
#                     continue 
                    
#             hashmap=set()
            
#             for j in range(i+1,len(nums)):
#                 third = -(nums[i]+nums[j])
#                 # rem = target - third
#                 if third in hashmap:    
#                     temp =[nums[i],nums[j],third]
#                     st.add(tuple(temp))
#                 hashmap.add(nums[j])             
                
#         ans = list(st)
#         return ans

    #above code need more space 
    