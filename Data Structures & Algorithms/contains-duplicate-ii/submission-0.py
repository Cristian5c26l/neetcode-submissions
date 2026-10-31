class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Time Complexity: O(n), due to the for
        # Space Complexity: O(n), due to the set

        # Pattern: Fixed Sliding Window

        window = set()# curr window of size <= k
        L = 0
        # window 
        for R in range(len(nums)):

            if R - L > k:
                window.remove(nums[L])
                L += 1

            if nums[R] in window and R - L <= k:# nums[R] in window means nums[i] (nums[R]) is equal to a nums[j] (stored in window)
                return True

            window.add(nums[R])

        return False