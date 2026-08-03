class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        L, R = 0, len(nums) - 1

        # Binary Search
        while L <= R:
            mid = (L + R) // 2# For example: mid_index = 6 + 10 // 2 = 8

            if target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else:
                return mid

        return -1
        