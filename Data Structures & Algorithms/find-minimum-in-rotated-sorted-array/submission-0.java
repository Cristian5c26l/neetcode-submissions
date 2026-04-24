class Solution {
    public int findMin(int[] nums) {
        int min = Integer.MAX_VALUE;

        // O(n) (solucion trivial, que a su vez es la fuerza bruta)
        for(int num: nums) {
            min = Math.min(min, num);
        }

        return min;
    }
}
