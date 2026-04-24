class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        int longest = 0;
        for(Integer num: set) {

            
            if(!set.contains(num - 1)) {// It's a sequence
                int length = 1;
                while(set.contains(num + length)) {
                    length++;
                }

                longest = Math.max(longest, length);
            }

        }

        return longest;

    }
}
