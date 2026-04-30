class Solution {
public:
    void helper(vector<int>& nums, int idx, vector<int>& ds, vector<vector<int>>& ans, int target){
        int n = nums.size();
        if(target == 0){
            ans.push_back(ds);
            return;
        }

        for(int i = idx; i < n; i++){
            if(i > idx && nums[i] == nums[i-1]) continue;
            if(nums[i] > target) break;
            ds.push_back(nums[i]);
            helper(nums,i+1,ds,ans,target-nums[i]);
            ds.pop_back();
        }

    }
    vector<vector<int>> combinationSum2(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<int> ds;
        vector<vector<int>> ans;
        helper(nums,0,ds,ans,target);
        return ans;
    }
};
