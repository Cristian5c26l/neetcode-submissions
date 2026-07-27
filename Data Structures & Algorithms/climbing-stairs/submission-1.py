class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climbStairsDPTopDown(n, cache):# Dynamic Programming based on Memoization (cache) approach which starts at Top and go Down
            
            if n in cache:
                return cache[n]

            if n < 0:
                return 0

            if n == 0:
                return 1

            cache[n] = climbStairsDPTopDown(n - 2, cache) + climbStairsDPTopDown(n - 1, cache)

            return cache[n] 
        
        cache = {}
        return climbStairsDPTopDown(n, cache)