class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int left = 0;
        int right = 0;
        Set<Character> slidingWindow = new HashSet<>();
        int longestSubstr = 0;

        while(right < s.length()) {
            
            while(slidingWindow.contains(s.charAt(right))) {
                slidingWindow.remove(s.charAt(left));
                left++;
            }

            slidingWindow.add(s.charAt(right));
            longestSubstr = Math.max(longestSubstr, right + 1 - left);

            right++;
        }

        return longestSubstr;
    }
}
