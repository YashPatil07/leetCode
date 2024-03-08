class Solution {
public:
    int uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int> umap;
        unordered_set<int> uset;
        for(auto num:arr){
            umap[num]++;
            
        }
        for(auto u:umap){
            cout<<u.first<<" "<<u.second<<" "<<endl;
        }

        for(auto i : umap){
            if(!uset.insert(i.second).second) return false; 
        }
    return true;
    }
};