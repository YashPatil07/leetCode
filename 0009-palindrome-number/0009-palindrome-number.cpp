class Solution {
public:
    bool isPalindrome(int x) {
    long long int rev=0;
    long long int dup=x;
    if(dup<0){
        return 0;
    }
    while(x!=0){
        int a=x%10;
        rev=(rev*10)+a;
        x/=10;
    }
    
    if(dup==rev){
        return 1;
    }
    else{
        return 0;
    }
    }
};