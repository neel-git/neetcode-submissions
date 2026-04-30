class Solution {
public:
    void helper(vector<int>& nums, int idx, vector<vector<int>>& ans, vector<int> &ds){
        int n = nums.size();
        if(idx >= n){
            ans.push_back(ds);
            return;
        }

        ds.push_back(nums[idx]);
        helper(nums,idx+1,ans,ds);
        ds.pop_back();
        helper(nums,idx+1,ans,ds);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> ds;
        helper(nums,0,ans, ds);
        return ans;
    }
};
