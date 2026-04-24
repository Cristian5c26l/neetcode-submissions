class Solution {
    public int characterReplacement(String s, int k) {
        
        int left = 0, right = 0;
        int longestSubstrWithRepeatingCharacterReplacement = 0;
        int maxFreq = 0;
        int curLength;
        Map<Character, Integer> freqs = new HashMap<>();

        while(right < s.length()) {

            Character c = s.charAt(right);
            freqs.put(c, freqs.getOrDefault(c, 0) + 1);
            maxFreq = Math.max(maxFreq, freqs.get(c));

            curLength = right - left + 1;

            if(curLength - maxFreq > k) {

                freqs.put(s.charAt(left), freqs.get(s.charAt(left)) - 1);
                left++;
                curLength = right - left + 1;
            } 

            longestSubstrWithRepeatingCharacterReplacement = Math.max(longestSubstrWithRepeatingCharacterReplacement, curLength);
                
            right++;

        }

        return longestSubstrWithRepeatingCharacterReplacement;

    }
}
