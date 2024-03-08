class Solution {
public:
    bool isPowerOfTwo(int n) {      ////MOST IMP:- check Constraints every time 
        for(int i=0;i<=30;i++){                   //    some times we assume it or ignor 
            int ans = pow(2,i);
            if(ans == n){
                return true;
            }
        }
        return false;
    }
};