class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        frequency ={}
        result=[]
        for number in nums:
            if number in frequency:
                frequency[number]+=1
            else:
                frequency[number]=1
         
        for key,value in frequency.items():
            if value > (n/3) :
                result.append(key)

        return result        
        