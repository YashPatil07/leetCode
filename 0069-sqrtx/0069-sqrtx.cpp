class Solution {
public:
long long int binarySearch(int n){
        int s = 0;
        int e = n;
        long long int ans = -1;
        long long int mid = s + (e-s)/2;
              
        while(s<=e){
            long long int multi = mid * mid;  
            if(multi == n) 
                return mid;
                
            if(multi < n){
               ans=mid;
               s=mid+1;
            }
            else{
            e = mid - 1; 
            }
        mid = s+(e-s)/2;
    }
    return ans;
    }
 int mySqrt(int x) {
        return binarySearch(x);
 }
};