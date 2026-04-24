class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Fuerza bruta O(m * n)
        for(int i = 0; i < matrix.length; i++) { // O(m)
            for(int j = 0; j < matrix[i].length; j++) {// O(n)
                if(matrix[i][j] == target) {
                    return true;
                }
            }
        }

        return false;
    }
}
