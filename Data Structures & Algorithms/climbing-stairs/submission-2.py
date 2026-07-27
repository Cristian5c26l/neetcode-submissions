class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climbStairsDPBottomUp(n):# Dynamic Programming based on Bottom Up (Tabulation) approach which starts at Bottom (Case Bases) and go Up
            
            tabulation = {-1: 0, 0: 1}

            if n < 1 and n in tabulation:
                return tabulation[n]

            i = 1
            while i <= n:
                tabulation[i] = tabulation[i - 2] + tabulation[i - 1]
                i += 1 
            
            return tabulation[n]
        
        return climbStairsDPBottomUp(n)