class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Optimal solution
        # Time Complexity: O(n)
        # Space Complexity: O(n) (due to result array of size n and the stack of size n in case of temperatures = [30,20,10])
        
        # Example: temperatures = [38, 30, 40] or [30, 30]
        result = [0] * len(temperatures)
        stack = []# Stack which stores indexes which references temperatures from higher to lower
        for i, current_temperature in enumerate(temperatures):
            
            while len(stack) > 0 and current_temperature > temperatures[stack[-1]]:
                lower_temperature_index = stack.pop()
                result[lower_temperature_index] = i - lower_temperature_index

            stack.append(i)
            
        return result