class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
          vector<int>ans;

        // make the numbers negative and simulteneously check for the negative number i.e Duplicate number

        for(int i = 0;i<nums.size();i++){
            int num = abs(nums[i]);

            if(nums[num - 1] < 1 ){
                ans.push_back(num);
            }
            // cout<<nums[num-1]<<" "<<endl;
            nums[num-1] = nums[num-1] * (-1);
            // cout<<nums[num-1]<<" ";
        }
        return ans;
    }
};