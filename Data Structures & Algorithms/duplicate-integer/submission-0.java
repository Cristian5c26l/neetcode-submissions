class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        // Hash Set
        Set<Integer> setNums = new HashSet<>();

        for(int num: nums) {
            if(setNums.contains(num)) {
                return true;
            }

            setNums.add(num);
        }

        return false;

    }
}