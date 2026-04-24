class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> freqMap = new HashMap<>();

        // Build FrequencyMap (O(n))
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Initializing Bucket (O(n))
        List<List<Integer>> bucket = new ArrayList<>(Collections.nCopies(nums.length + 1, null));

        for (int freq = 0; freq < bucket.size(); freq++) {
            bucket.set(freq, new ArrayList<>());
        }

        // Building Bucket (O(n))
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            bucket.get(freq).add(num);
        }

        // Building final array with the k numbers with most frequence
        int[] top = new int[k];// top.length = 2 if k == 2
        int count = 0;
        for (int freq = bucket.size() - 1; freq >= 0 && count < k; freq--) {

            for (int i = 0; i < bucket.get(freq).size(); i++) {
                if (count == k) break;
                top[count] = bucket.get(freq).get(i);
                count++;
            }

        }

        return top;

    }
}
