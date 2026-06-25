class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force solution
        # Time Complexity: O(n*n) (Worst case due to for example the [40,39,38,37,36] array of temperatures)
        # Space Complexity: O(n) (due to)
        
        result = [0] * len(temperatures)
        for i, current_temperature in enumerate(temperatures):
            for j in range(i + 1, len(temperatures)):# 4 iterations + 3 iterations + 2 iterations + 1 iterations = n*(n-1)/2 = O(n*n)
                if current_temperature < temperatures[j]:
                    result[i] = j - i#days_until_warmer_temperature = j - i
                    break
            
        return result