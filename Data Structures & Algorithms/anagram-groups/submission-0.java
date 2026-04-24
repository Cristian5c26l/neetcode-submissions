class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> anagramsGroups = new HashMap<>();

        for(String str: strs) {// m strings

            int[] freqCharacters = new int[26];
            for(char c: str.toCharArray()) {// n (longest string)
                freqCharacters[c - 'a']++;
            }

            if(!anagramsGroups.containsKey(Arrays.toString(freqCharacters))) {
                List<String> newAnagramGroup = new ArrayList<>();
                newAnagramGroup.add(str);
                anagramsGroups.put(Arrays.toString(freqCharacters), newAnagramGroup);
            } else {
                anagramsGroups.get(Arrays.toString(freqCharacters)).add(str);
            }


        }

        return new ArrayList<>(anagramsGroups.values());

    }
}
