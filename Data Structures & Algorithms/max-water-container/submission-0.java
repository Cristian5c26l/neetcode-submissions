class Solution {
    public int maxArea(int[] heights) {
        
        int left = 0;
        int right = heights.length - 1;

        int maximumAmountWaterArea = 0;

        while(left < right) {
            int base = right - left;
            int smallerHeight = Math.min(heights[left], heights[right]);// maximum Amount of water of the container depends on the base and height (smaller height, because I may not slant the container)
            maximumAmountWaterArea = Math.max(maximumAmountWaterArea, base * smallerHeight);

            if(heights[left] < heights[right]) {
                left++;
            } else if(heights[left] > heights[right]) {
                right--;
            } else {
                left++;// or right--
            }

        }

        return maximumAmountWaterArea;
    }
}
