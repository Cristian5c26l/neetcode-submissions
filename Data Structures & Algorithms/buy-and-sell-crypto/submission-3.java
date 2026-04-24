class Solution {
    public int maxProfit(int[] prices) {
        
        int start = 0, end = 1, profit = 0;

        while(end < prices.length) {

            if(prices[start] < prices[end]) {
                profit = Math.max(profit, prices[end] - prices[start]);
            } else {
                start = end;
            }

            end++;
        }

        return profit;


    }
}
