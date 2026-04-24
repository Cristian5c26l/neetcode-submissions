class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int area = 0;

        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i <= n; i++) {
            int height = (i == n) ? 0 : heights[i];

            while (!stack.isEmpty() && height < heights[stack.peek()]) {
                int barPosition = stack.pop();
                int barHeight = heights[barPosition];

                int left = stack.isEmpty() ? -1 : stack.peek();

                int width = i - left - 1;
                area = Math.max(area, barHeight * width);
            }

            stack.push(i);
        }

        return area;
    }
}
