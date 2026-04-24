class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        int[] perm = new int[26];
        int[] window = new int[26];

        for(int i = 0; i < s1.length(); i++) {
            perm[s1.charAt(i) - 'a']++;
        }

        int left = 0, right = 0;

        while(right < s2.length()) {

            window[s2.charAt(right) - 'a']++;

            int slidingWindow = right + 1 - left;

            if(slidingWindow > s1.length()) {
                window[s2.charAt(left) - 'a']--;
                left++;
            }

            if(Arrays.toString(perm).equals(Arrays.toString(window))) {
                return true;
            }

            right++;
        }

        return false;

    }
}
