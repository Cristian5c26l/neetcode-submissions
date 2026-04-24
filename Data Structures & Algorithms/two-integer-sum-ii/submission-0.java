class Solution {
    public int[] twoSum(int[] numbers, int target) {// numbers is a sorted array in increasing-order
        
        int left = 0;
        int right = numbers.length - 1;

        int[] indexes = new int[2]; // stores 1-indexed (position + 1) of the two numbers which its sum is equal to target
        int sum;
        while(left < right) {// It is logical that numbers[left] < numbers[right]

            sum = numbers[left] + numbers[right];

            if( sum == target) {// indexes of two numbers
                indexes[0] = left + 1;
                indexes[1] = right + 1; 
                break;
            }

            if(sum > target) {
                right--;// Try with a number with less value
            } else {
                left++;// Try with a number with more value
            }

        }

        return indexes;

    }
}
