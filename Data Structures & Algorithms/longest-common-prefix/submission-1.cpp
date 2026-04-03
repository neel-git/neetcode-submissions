class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        sort(strs.begin(),strs.end());
        string first_word = strs[0];
        string last_word = strs[n-1];
        string ans = "";
        int m = min(first_word.length(), last_word.length());

        for(int i = 0; i < m; i++){
            if(first_word[i] != last_word[i]){
                break;
            }
            ans += first_word[i];
        }
        return ans;
    }
};