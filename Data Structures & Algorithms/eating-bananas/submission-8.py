class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Optimal Solution
        # Time Complexity: O(nlogm)
        # Space Complexity: O(1)

        # piles[i] is the number of bananas in the ith pile. 
        # h represents the number of hours the bananas have to be eaten.
        # "m" is the maximum "k" rate of eating bananas per hourn
        # Range low - high contains values of "k".

        m = max(piles) # O(n)
        min_k = m
        low = 1
        high = m
        while low <= high:# O(logm). This is binary search
            k = (low + high) // 2

            eating_time = 0
            for bananas in piles:# O(n)
                hours = math.ceil(float(bananas) / k)# Calculate how many hours takes eating all "bananas" of the ith pile, considering a rate of k bananas per hour
                eating_time += hours

            if eating_time > h:
                low = k + 1# Increase the speed (bananas-perhour, which is k) of eating all bananas
            else:# eating_time <= h
                min_k = k
                high = k - 1

        return min_k



        