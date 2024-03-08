class Solution {
public:
    int findComplement(int num) {
            int m=num;
        int mask=0;
        if(num==0) return 1;

        while(m!=0){             // for mask 
            mask=(mask<<1)|1;
            m=m>>1;
        }

        int ans = ( ~num ) & mask; //1's complement and mask to get the output 
        return ans;
    }
};