class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        // O(logm) + O(logn) = O(log(m * n))
  
        int lowRow = 0;
        int highRow = matrix.length - 1;

        //O(logm) Binary search en las filas de la matriz para buscar la fila donde caiga el target
        int rowTarget = -1;
        while(lowRow <= highRow) {
            int midRow = lowRow + ((highRow - lowRow) / 2);
            int firstNumberMidRow = matrix[midRow][0];
            int lastNumberMidRow = matrix[midRow][matrix[midRow].length - 1];

            if(target >= firstNumberMidRow && target <= lastNumberMidRow) {
                rowTarget = midRow;
                break;
            } else if(target > lastNumberMidRow) {
                lowRow = midRow + 1;
            } else if(target < firstNumberMidRow) {
                highRow = midRow - 1;
            }
        }

        // O(1)
        if(rowTarget == -1) {
            return false;
        }

        // O(logn)
        int low = 0;
        int high = matrix[rowTarget].length - 1;

        while (low <= high) {

            int midIndex = low + ((high - low) / 2);

            if (matrix[rowTarget][midIndex] == target) {
                return true;
            } else if (target > matrix[rowTarget][midIndex]) {
                low = midIndex + 1;
            } else if (target < matrix[rowTarget][midIndex]) {
                high = midIndex - 1;
            }

        }

        return false;
    }
}
