class Solution:
    def search(self, nums: List[int], target: int) -> int:


        # Binary Search
        # Time Complexity: O(logn)

        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = R + L // 2
            if target < nums[mid]:
                R = mid - 1
            elif target > nums[mid]:
                L = mid + 1
            else:
                return mid#L = R + 1

        return -1
        