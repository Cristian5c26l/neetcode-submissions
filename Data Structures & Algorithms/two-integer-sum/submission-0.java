class Solution {

    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> indicesMap = new HashMap<>();

        for(int i = 0; i < nums.length ; i++) {
            
            int num = nums[i];
            int complement = target - num;

            if(indicesMap.containsKey(complement)) {
                return new int[]{indicesMap.get(complement), i};
            }

            indicesMap.put(num, i);

        }

        return new int[]{};

        //return two different indices such that nums[i] + nums[j] equals to target;

    }

}
