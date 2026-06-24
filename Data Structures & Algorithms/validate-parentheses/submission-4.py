class Solution:
    def isValid(self, s: str) -> bool:

        # Brute force Solution
        # Time complexity: O(n*n)
        # Space complexity: O(n)

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        
        return s == ''