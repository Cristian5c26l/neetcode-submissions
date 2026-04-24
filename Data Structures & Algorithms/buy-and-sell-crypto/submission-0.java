class Solution {
    public int maxProfit(int[] prices) {
        
        int start = 0, end = 0, profit = 0;

        while(end < prices.length) {

            while(end < prices.length - 1 && prices[start] < prices[end + 1]) {
                end++;
                profit = Math.max(profit, prices[end] - prices[start]);
            }


            end++;
            start = end;


        }

        return profit;


    }
}
