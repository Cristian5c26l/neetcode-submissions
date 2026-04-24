class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;// n barras
        int area = -1;

        for(int i = 0; i < n; i++) {// O(n)

            int height = heights[i];// Analizar cada barra actual "i"
            
            // O(n) entre los 2 whiles porque se revisan todas las alturas de las barras que estan a la izquierda y derecha del actual 
            int left = i;
            while(left > 0 && heights[left - 1] >= height) {// Expandir a la izquierda, mientras la barra izquierda (left - 1 = i - 1) de la actual (la "i"), sea mayor a dicha actual
                left--;
            }
            
            int right = i;
            while(right < n - 1 && heights[right + 1] >= height) {// Expandir a la derecha, mientras la barra a la derecha (right + 1 = i + 1) de la actual (la "i"), sea mayor a dicha actual
                right++;
            }

            area = Math.max(area, height * (right - left + 1));

        }

        return area;
    }
}
