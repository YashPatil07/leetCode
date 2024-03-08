class Solution {
public:
    int bitwiseComplement(int n) {
        int m=n;
        int mask=0;
        if(n==0) return 1;  // edge case

        while(m!=0){             // for mask 
            mask=(mask<<1)|1;
            m=m>>1;
        }

        int ans = ( ~n ) & mask; //1's complement and mask to get the output 
        return ans;
    }
};