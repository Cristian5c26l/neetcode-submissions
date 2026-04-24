class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        int[] max = new int[nums.length - k + 1];
        int maxPosition = 0;
        int left = 0;
        int slidingWindow;

        Deque<Integer> deque = new ArrayDeque<>();// Monotonic Queue (cola con operaciones de insercion/eliminacion/extraccion al frente y al final... Su frente es el elemento mayor. El ultimo es el elemento menor)
        // O(n)
        for(int right = 0; right < nums.length; right++) {
            
            
            while(!deque.isEmpty() && nums[deque.peekLast()] <= nums[right]) {
                
                // O(1)
                deque.pollLast();// Remover indices inutiles
            }
            
            deque.offerLast(right);

            slidingWindow = right - left + 1;
            if(slidingWindow == k) {
                
                while(deque.peekFirst() < left) {
                    // O(1)
                    deque.pollFirst();
                }

                // O(1)
                max[maxPosition] = nums[deque.peekFirst()];
                maxPosition++;    

                left++;
            }

            
            
        }

        return max;

    }
}
