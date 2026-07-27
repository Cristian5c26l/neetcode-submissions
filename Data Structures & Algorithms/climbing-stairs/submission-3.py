class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climbStairsDPBottomUp(n):# Dynamic Programming based on Bottom Up approach which starts at Bottom (Case Bases) and go Up
            
            tabulation = {-1: 0, 0: 1}

            i = 1
            while i <= n:
                temp = tabulation[0]
                tabulation[0] = tabulation[-1] + tabulation[0]
                tabulation[-1] = temp
                i += 1 
            
            return tabulation[0]
        
        return climbStairsDPBottomUp(n)