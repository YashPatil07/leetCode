class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>m;
        int s=nums.size();
        for(int i=0;i<s;++i){
        if(m.find(target-nums[i])==m.end()){
            m[nums[i]]=i;
        }
        else
            return {i,m[target-nums[i]]};
        }
        return {};
    //      int sum=0;
    //     for(int i=0;i<s;++i){
    //         for(int j=0;j<s;j++){
    //             cout<<"i-"<<i<<" "<<"j- "<<j<<endl;
    //             sum=sum+nums[j];
    //             cout<<"sum"<<sum<<endl;
    //             while(sum>target && i<j){
    //                 sum-=nums[i];
    //                 i++;
    //             }
    //             if(sum==target){
    //                 return {i,j};
    //             }
    //         }
    //     }
    //  return {-1};

    // }
    }
};