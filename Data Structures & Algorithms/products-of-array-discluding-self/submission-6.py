class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(2n) = O(n)
        res = [0] * len(nums)
        res[0] = 1
        # Prefix product
        ac_prod = 1
        for i in range(len(nums) - 1):# O(n)
            ac_prod *= nums[i]
            res[i + 1] = ac_prod

        # Postfix product
        ac_prod = 1
        for i in range(len(nums) - 1, 0, -1):# Start from the last, to the first, on reverse
            ac_prod *= nums[i]
            res[i - 1] *= ac_prod
    
        return res