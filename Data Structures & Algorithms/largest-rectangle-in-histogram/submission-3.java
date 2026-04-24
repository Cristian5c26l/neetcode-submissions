class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;// n barras
        int area = 0;

        Deque<Integer> stack = new ArrayDeque<>();//stack que en el algoritmo se juega con ella para que sea monotonica creciente
        int left = -1; // valor -1 para indicar que la stack esta vacia

        for(int i = 0; i < n; i++) {// O(n)

            int height = heights[i];// Analizar cada barra actual "i"

            while(!stack.isEmpty() && height < heights[stack.peek()]) {// heights[stack.peek()] es una barra la cual cuando height < heights[stack.peek(), se forma un rectangulo comun... Todo: repasar aqui

                int barHeightPending = heights[stack.peek()];
                int barPositionPending = stack.pop();
                

                if(stack.isEmpty()) {
                    left = -1;
                } else {
                    left = stack.peek();
                }

                area = Math.max(area, barHeightPending * (i - left - 1));
            }

            stack.push(i);

            if(i + 1 == n) {
                height = 0;
                i = n;

                while(!stack.isEmpty() && height < heights[stack.peek()]) {// heights[stack.peek()] es una barra la cual cuando height < heights[stack.peek(), se forma un rectangulo comun

                    int barHeightPending = heights[stack.peek()];
                    int barPositionPending = stack.pop();
                    
                    if(stack.isEmpty()) {
                        left = -1;
                    } else {
                        left = stack.peek();
                    }

                    area = Math.max(area, barHeightPending * (i - left - 1));

                }

            }


        }

        return area;
    }
}
