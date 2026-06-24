class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # Optimal solution
        # Time complexity: O(n)
        # Space complexity: O(n)

        n = len(nums)# n is the length of the array nums
        ans = [0] * (2*n)
        for i in range(n):# O(n)
            ans[i], ans[i + n] = nums[i], nums[i]

        return ans