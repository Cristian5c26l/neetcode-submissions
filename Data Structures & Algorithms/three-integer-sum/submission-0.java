class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        // O(nlogn) (action of sort is important to solve this exercise)
        Arrays.sort(nums);// -4,-1,-1,0,1,2

        List<List<Integer>> output = new ArrayList<>();

        // O(n*n)
        for(int i = 0; i < nums.length ; i++) {
            
            if(i > 0 && nums[i] == nums[i - 1]) {// Preventing from repeating triplet since its first element
                continue;
            }

            // nums[i] + nums[j] + nums[k] = 0
            // -nums[i] = nums[j] + nums[k]
            int j = i + 1;
            int k = nums.length - 1;
            int target = (nums[i]) * (- 1);// First element of the triplet
            while(j < k) {
                
                if(nums[j] + nums[k] == target) {
                    List<Integer> triplet = new ArrayList<>();
                    //System.out.println("A: "+nums[i]+". B: "+nums[j]+". C: "+nums[k]);
                    output.add(List.of(nums[i], nums[j], nums[k]));

                    // This is important (try to understand it)
                    while(j < k && nums[j] == nums[j+1]) {// Do this if the next num is equal to the current
                        j++;
                    }

                    while(j < k && nums[k] == nums[k-1]) {// // Do this if the previous num is equal to the current
                        k--;
                    }

                    j++;
                    k--;
                } else if(nums[j] + nums[k] > target) {
                    k--;// decrease to get a nums[k] with min value
                } else if(nums[j] + nums[k] < target) {
                    j++;
                }
            
            }
        }

        return output;

    }
}
