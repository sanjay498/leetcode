class Solution {
    public int maxProfit(int[] prices) {
        int total = 0;
        int buy = 0, sell = 1;
        int n = prices.length;

        while (sell < n) {
            if (prices[buy] < prices[sell]) {
             
                total += prices[sell] - prices[buy];
            }
         
            buy++;
            sell++;
        }

        return total;
    }
}
