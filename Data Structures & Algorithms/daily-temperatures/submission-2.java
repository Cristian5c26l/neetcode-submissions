class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        
        int[] futuresDaysUntilWarmerTemperature = new int[temperatures.length];

        Deque<Integer> monotonicStack = new ArrayDeque<>();

        // O(n*n)
        // O(n)
        for(int i = 0; i < temperatures.length; i++) {
            
            //int currentTemperature = temperatures[i];
            
            while(!monotonicStack.isEmpty() && temperatures[i] > temperatures[monotonicStack.peek()]) {
                int ithDay = monotonicStack.pop();// O(1)

                futuresDaysUntilWarmerTemperature[ithDay] = i - ithDay;
            }

            monotonicStack.push(i);

        }

        return futuresDaysUntilWarmerTemperature;

    }
}
