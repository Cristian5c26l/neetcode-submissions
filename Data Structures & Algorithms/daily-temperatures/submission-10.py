class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Optimal Force Solution
        # Time Complexity: O(n)
        # Space Complexity: O(n) for extra space, O(n) for the output array

        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):

            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:# stack_day is a prev_ith_day
                prev_ith_day = stack.pop()# Pop Operation runs in O(1) time
                res[prev_ith_day] = i - prev_ith_day# i - prev_ith_day is the days until appears a warmer temperature greater than the ith temperature (temperatures[i])

            stack.append(i)# Push Operation runs in O(1) time

        # Empty stack (not necessary)
        while stack:# while len(stack) > 0
            res[stack.pop()] = 0         

        return res