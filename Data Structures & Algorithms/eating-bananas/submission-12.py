class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Input: [1,4,3,2]. In the 1th pile there are 4 bananas

        # Time Complexity: O(nlogm)

        L, R = 1, max(piles)# min_k is always between 1 and the ith pile that has more bananas than the others
        min_k = R
        while L <= R:# O(logm)
            k = (L + R) // 2
            hours_when_eat_k = self.hours_elapsed_when_eating_k_bananas(k, piles)# O(n). elapsed = transcurred
            if hours_when_eat_k > h:
                L = k + 1# Koko lates more hours than the h when he eats k bananas. So, he should eat more k bananas to accomplish the number of hours within h
            else:# hours_when_eat_k <= h:
                min_k = k
                R = k - 1# Keep finding the min_k

        return min_k


    
    def hours_elapsed_when_eating_k_bananas(self, k, piles):

        hours = 0
        for bananas in piles:# O(n), where n is the size of the input array piles
            hours += math.ceil(bananas / k) # math.ceil(bananas / k) represents the number of hours that koko takes to eat k bananas, i.e, the total of hours he will eat all the bananas if he eat k of the bananas in 1 hour. Sample: [1,4,3,2], so hours = 1 + 2 + 2 + 1 = 6

        return hours


        