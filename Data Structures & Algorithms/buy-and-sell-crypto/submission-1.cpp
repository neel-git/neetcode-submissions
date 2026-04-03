class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int buyingPrice = prices[0];
        int profit = 0;
        for(int i = 1; i < n; i++){
           if(prices[i] < buyingPrice){
            buyingPrice = prices[i];
           } else if(prices[i] - buyingPrice > profit){
            profit = prices[i] - buyingPrice;
           }
        }
        return profit;
    }
};
