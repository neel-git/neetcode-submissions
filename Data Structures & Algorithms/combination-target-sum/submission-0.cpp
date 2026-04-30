class Solution {
public:
    void helper(vector<int>& nums, int idx, vector<int>& ds, vector<vector<int>>& ans, int target){
        int n = nums.size();
        if(idx == n){
            if(target == 0){
                ans.push_back(ds);
            }
            return;
        }

        if(nums[idx] <= target){
            ds.push_back(nums[idx]);
            helper(nums,idx,ds,ans,target-nums[idx]);
            ds.pop_back();
        }
        helper(nums,idx+1,ds,ans,target);
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> ds;
        vector<vector<int>> ans;
        helper(nums,0,ds,ans,target);
        return ans;
    }
};
