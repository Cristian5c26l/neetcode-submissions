class Solution {
    public int search(int[] nums, int target) {

        int low = 0;
        int high = nums.length - 1;
        int midIndex = (high - low) / 2;
        
        while(midIndex >=low && midIndex <= high ){

            System.out.println("nums[midIndex] = " + nums[midIndex]);

            if(nums[midIndex] == target) {
                return midIndex;
            }

            if(target > nums[midIndex]) {
                low = midIndex + 1;
                midIndex = low + ((high - low) / 2);
            } else if(target < nums[midIndex]) {
                high = midIndex - 1;
                midIndex = low + ((high - low) / 2);
            }

        }

        return -1;

    }
}
