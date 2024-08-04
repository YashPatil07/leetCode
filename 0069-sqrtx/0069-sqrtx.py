class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        mid = start +(end-start)//2
        ans=-1
        while start<=end:
            multi = mid * mid
            if multi == x:
                return mid
            elif multi < x:
                ans=mid
                start = mid+1
            else:
                end=mid-1
            mid=start+(end-start)//2
        return ans