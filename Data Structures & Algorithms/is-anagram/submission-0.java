class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()) return false;

        Map<Character, Integer> frequency = new HashMap<>();

        for(char c: s.toCharArray()) {            
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }

        for(char c: t.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, -1) - 1);
        }

        for(Map.Entry<Character, Integer> entry: frequency.entrySet()) {
            int characterFrequency = entry.getValue();

            if(characterFrequency != 0) return false;
        }

        return true;

    }
}
