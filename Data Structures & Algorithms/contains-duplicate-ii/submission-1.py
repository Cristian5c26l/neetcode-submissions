class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Time Complexity: O(n), due to the for
        # Space Complexity: O(n), due to the set

        # Pattern: Fixed Sliding Window
        # Input: nums = [1,2,3,1] or [1,5,3,0,5], with k = 3 (Sample: i - j = 4 - 1 = 3)

        window = set()# curr window of size <= k
        L = 0
        for R in range(len(nums)):

            if R - L > k:# 2. Shrink the window
                window.remove(nums[L])
                L += 1

            if nums[R] in window and R - L <= k:# 1. if we found a num duplicated and within a valid window size (R - L = window size) 
                return True 

            window.add(nums[R]) # 0. Expand the window

        return False