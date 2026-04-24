class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        int[] max = new int[nums.length - k + 1];
        int maxPosition = 0;
        int left = 0;
        int slidingWindow;

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);// a, b) -> b[0] - a[0] significa ordenar de forma descendente (la raiz tiene el numero mayor)

        // O(nlogn)
        for(int right = 0; right < nums.length; right++) {
            
            slidingWindow = right - left + 1;
            
            // O(logn)
            maxHeap.offer(new int[]{nums[right], right});// num, indexOfNum

            if(slidingWindow == k) {
                
                while(maxHeap.peek()[1] < left) {
                    // O(logn)
                    maxHeap.poll();
                }

                //if(maxHeap.peek()[1] >= left) {
                // O(1)
                max[maxPosition] = maxHeap.peek()[0];
                maxPosition++;    

                
                left++;
            }

            
            
        }

        return max;

    }
}
