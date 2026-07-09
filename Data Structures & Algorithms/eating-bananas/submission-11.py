class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Optimal Solution
        # Time Complexity: O(nlogm)
        # Space Complexity: O(1)

        # piles[i] is the number of bananas in the ith pile. 
        # h represents the number of hours the bananas have to be eaten.
        # "k" represents the eating rate of bananas-per-hour
        # "m" is the maximum "k" rate of eating bananas per hour. This is one of the insights of this exercise
        # Range low - high contains values of "k".

        # The goal is find the minimum integer k such that you can eat all the bananas within h hours.

        m = max(piles) # O(n)
        min_k = m
        low = 1
        high = m

        # O(nlogm)
        while low <= high:# O(logm). This is binary search - search range
            k = (low + high) // 2

            eating_time = 0
            for bananas in piles:# O(n)
                hours = math.ceil(float(bananas) / k)# Calculate how many hours takes eating all "bananas" of the ith pile, considering an eating rate of k bananas per hour
                eating_time += hours

            if eating_time > h:
                low = k + 1# Increase the speed (bananas-perhour, which is k) of eating all bananas
            else:# eating_time <= h
                min_k = k
                high = k - 1

        return min_k

        # Input: piles = [1,4,3,2], h = 9
        # Output: k = 2
        # Explanation: With an eating rate of k = 2, you can eat the bananas in 6 hours (1 bananas in 1 hour, 4 bananas in 2 hours, 3 bananas in 2 hours, 2 bananas in 1 hours. Each hours value is calculated with math.ceil(float(bananas) / k)). With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.



        